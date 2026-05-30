import swisseph as swe
import ephem
import math
from datetime import datetime, date, timedelta
import pytz
from typing import Tuple, Optional, Dict, List

# Set ephemeris path
swe.set_ephe_path('')

PLANETS = {
    'Sun': swe.SUN, 'Moon': swe.MOON, 'Mars': swe.MARS,
    'Mercury': swe.MERCURY, 'Jupiter': swe.JUPITER, 'Venus': swe.VENUS,
    'Saturn': swe.SATURN, 'Rahu': swe.TRUE_NODE, 'Ketu': -1
}

NAKSHATRA_NAMES = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
    "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
    "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati",
    "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
    "Uttara Ashadha", "Shravana", "Dhanishtha", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

RASHI_NAMES = [
    "Mesha", "Vrishabha", "Mithuna", "Karka", "Simha", "Kanya",
    "Tula", "Vrishchika", "Dhanu", "Makara", "Kumbha", "Meena"
]

TITHI_NAMES = [
    "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami",
    "Shashthi", "Saptami", "Ashtami", "Navami", "Dashami",
    "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima",
    "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami",
    "Shashthi", "Saptami", "Ashtami", "Navami", "Dashami",
    "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Amavasya"
]

YOGA_NAMES = [
    "Vishkambha", "Priti", "Ayushman", "Saubhagya", "Shobhana",
    "Atiganda", "Sukarma", "Dhriti", "Shula", "Ganda",
    "Vriddhi", "Dhruva", "Vyaghata", "Harshana", "Vajra",
    "Siddhi", "Vyatipata", "Variyana", "Parigha", "Shiva",
    "Siddha", "Sadhya", "Shubha", "Shukla", "Brahma",
    "Indra", "Vaidhriti"
]

KARANA_NAMES = [
    "Kimstughna", "Bava", "Balava", "Kaulava", "Taitila",
    "Garija", "Vanija", "Vishti", "Shakuni", "Chatushpada", "Naga"
]

MASA_NAMES = [
    "Chaitra", "Vaishakha", "Jyeshtha", "Ashadha", "Shravana",
    "Bhadrapada", "Ashwina", "Kartika", "Margashirsha", "Pausha",
    "Magha", "Phalguna"
]

VARA_NAMES = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

GOOD_YOGA = ["Priti", "Ayushman", "Saubhagya", "Shobhana", "Sukarma", "Dhriti",
             "Vriddhi", "Dhruva", "Harshana", "Siddhi", "Siddha", "Sadhya",
             "Shubha", "Shukla", "Brahma", "Indra"]

BAD_YOGA = ["Vishkambha", "Atiganda", "Shula", "Ganda", "Vajra",
            "Vyatipata", "Parigha", "Vaidhriti", "Vyaghata"]

GOOD_TITHI = [1, 2, 3, 5, 7, 10, 11, 13]
BAD_TITHI = [4, 8, 9, 14, 15, 19, 23, 28, 29, 30]

# Rahu Kaal in hours from sunrise (weekday 0=Sun)
RAHU_KAAL = {0: (4, 5), 1: (7, 8), 2: (2, 3), 3: (5, 6), 4: (1, 2), 5: (0, 1), 6: (8, 9)}
GULIKA_KAAL = {0: (6, 7), 1: (5, 6), 2: (4, 5), 3: (3, 4), 4: (2, 3), 5: (1, 2), 6: (7, 8)}
YAMAGANDA = {0: (2, 3), 1: (1, 2), 2: (0, 1), 3: (7, 8), 4: (6, 7), 5: (5, 6), 6: (4, 5)}

def datetime_to_jd(dt: datetime, tz_offset: float = 5.5) -> float:
    """Convert datetime to Julian Day (UTC)"""
    dt_utc = dt - timedelta(hours=tz_offset)
    return swe.julday(dt_utc.year, dt_utc.month, dt_utc.day,
                      dt_utc.hour + dt_utc.minute/60 + dt_utc.second/3600)

def get_ayanamsa(jd: float) -> float:
    """Get Lahiri ayanamsa"""
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    return swe.get_ayanamsa(jd)

def get_planet_lon(jd: float, planet: int) -> float:
    """Get sidereal longitude of planet"""
    if planet == -1:  # Ketu
        rahu_lon = swe.calc_ut(jd, swe.TRUE_NODE)[0][0]
        ayanamsa = get_ayanamsa(jd)
        return (rahu_lon - ayanamsa - 180) % 360
    result = swe.calc_ut(jd, planet)
    ayanamsa = get_ayanamsa(jd)
    return (result[0][0] - ayanamsa) % 360

def lon_to_nakshatra(lon: float) -> Tuple[str, int, float]:
    """Convert longitude to nakshatra, pada, and degree"""
    nakshatra_idx = int(lon / (360/27))
    pada = int((lon % (360/27)) / (360/27/4)) + 1
    deg_in_nak = lon % (360/27)
    return NAKSHATRA_NAMES[nakshatra_idx], pada, deg_in_nak

def lon_to_rashi(lon: float) -> Tuple[str, float]:
    """Convert longitude to rashi and degree within rashi"""
    rashi_idx = int(lon / 30)
    deg_in_rashi = lon % 30
    return RASHI_NAMES[rashi_idx % 12], deg_in_rashi

def get_tithi(jd: float) -> Tuple[int, str, str]:
    """Get tithi number (1-30), name, and paksha"""
    sun_lon = get_planet_lon(jd, swe.SUN)
    moon_lon = get_planet_lon(jd, swe.MOON)
    diff = (moon_lon - sun_lon) % 360
    tithi_num = int(diff / 12) + 1
    paksha = "Shukla" if tithi_num <= 15 else "Krishna"
    tithi_in_paksha = tithi_num if tithi_num <= 15 else tithi_num - 15
    tithi_name = TITHI_NAMES[tithi_num - 1]
    return tithi_num, tithi_name, paksha

def get_yoga(jd: float) -> Tuple[int, str]:
    """Get yoga number and name"""
    sun_lon = get_planet_lon(jd, swe.SUN)
    moon_lon = get_planet_lon(jd, swe.MOON)
    yoga_lon = (sun_lon + moon_lon) % 360
    yoga_idx = int(yoga_lon / (360/27))
    return yoga_idx + 1, YOGA_NAMES[yoga_idx]

def get_karana(jd: float) -> Tuple[int, str]:
    """Get karana"""
    sun_lon = get_planet_lon(jd, swe.SUN)
    moon_lon = get_planet_lon(jd, swe.MOON)
    diff = (moon_lon - sun_lon) % 360
    karana_idx = int(diff / 6) % 11
    return karana_idx + 1, KARANA_NAMES[karana_idx]

def get_sunrise_sunset(jd: float, lat: float, lon: float) -> Tuple[float, float]:
    """Get sunrise and sunset as JD"""
    try:
        geopos = (lon, lat, 0)
        ret_rise = swe.rise_trans(jd - 0.5, swe.SUN, geopos, 0, swe.CALC_RISE | swe.BIT_DISC_CENTER)
        ret_set = swe.rise_trans(jd - 0.5, swe.SUN, geopos, 0, swe.CALC_SET | swe.BIT_DISC_CENTER)
        sunrise_jd = ret_rise[1][0]
        sunset_jd = ret_set[1][0]
        return sunrise_jd, sunset_jd
    except:
        # Fallback approximation
        return jd + (6.0 - lon/15)/24, jd + (18.0 - lon/15)/24

def jd_to_local_time(jd: float, tz_offset: float = 5.5) -> str:
    """Convert JD to local time string"""
    dt = swe.jdut1_to_utc(jd, 1)
    hours = dt[3] + dt[4]/60 + dt[5]/3600 + tz_offset
    hours = hours % 24
    h = int(hours)
    m = int((hours - h) * 60)
    ampm = "AM" if h < 12 else "PM"
    h12 = h % 12 or 12
    return f"{h12:02d}:{m:02d} {ampm}"

def get_masa(jd: float) -> str:
    """Get Hindu lunar month"""
    sun_lon = get_planet_lon(jd, swe.SUN)
    masa_idx = int(sun_lon / 30) % 12
    return MASA_NAMES[masa_idx]

def get_vara(jd: float) -> str:
    """Get day of week"""
    # JD day 0 = Monday in Hindu calendar reckoning
    day_num = int(jd + 1.5) % 7
    return VARA_NAMES[day_num]

def get_rahu_kaal(jd: float, lat: float, lon: float, tz_offset: float = 5.5) -> Tuple[str, str]:
    """Get Rahu Kaal start and end times"""
    sunrise_jd, sunset_jd = get_sunrise_sunset(jd, lat, lon)
    day_duration = (sunset_jd - sunrise_jd) / 8  # 8 parts
    weekday = int(jd + 1.5) % 7
    slot = RAHU_KAAL[weekday][0]
    rk_start = sunrise_jd + slot * day_duration
    rk_end = rk_start + day_duration
    return jd_to_local_time(rk_start, tz_offset), jd_to_local_time(rk_end, tz_offset)

def get_gulika_kaal(jd: float, lat: float, lon: float, tz_offset: float = 5.5) -> Tuple[str, str]:
    """Get Gulika Kaal"""
    sunrise_jd, sunset_jd = get_sunrise_sunset(jd, lat, lon)
    day_duration = (sunset_jd - sunrise_jd) / 8
    weekday = int(jd + 1.5) % 7
    slot = GULIKA_KAAL[weekday][0]
    gk_start = sunrise_jd + slot * day_duration
    gk_end = gk_start + day_duration
    return jd_to_local_time(gk_start, tz_offset), jd_to_local_time(gk_end, tz_offset)

def get_yamaganda(jd: float, lat: float, lon: float, tz_offset: float = 5.5) -> Tuple[str, str]:
    """Get Yamaganda"""
    sunrise_jd, sunset_jd = get_sunrise_sunset(jd, lat, lon)
    day_duration = (sunset_jd - sunrise_jd) / 8
    weekday = int(jd + 1.5) % 7
    slot = YAMAGANDA[weekday][0]
    yg_start = sunrise_jd + slot * day_duration
    yg_end = yg_start + day_duration
    return jd_to_local_time(yg_start, tz_offset), jd_to_local_time(yg_end, tz_offset)

def get_abhijit_muhurta(jd: float, lat: float, lon: float, tz_offset: float = 5.5) -> Tuple[str, str]:
    """Get Abhijit Muhurta (auspicious midday)"""
    sunrise_jd, sunset_jd = get_sunrise_sunset(jd, lat, lon)
    midday = (sunrise_jd + sunset_jd) / 2
    duration = (sunset_jd - sunrise_jd) / 15  # 1/15 of day
    return jd_to_local_time(midday - duration/2, tz_offset), jd_to_local_time(midday + duration/2, tz_offset)

def get_brahma_muhurta(jd: float, lat: float, lon: float, tz_offset: float = 5.5) -> Tuple[str, str]:
    """Get Brahma Muhurta (96 mins before sunrise)"""
    sunrise_jd, sunset_jd = get_sunrise_sunset(jd, lat, lon)
    bm_end = sunrise_jd
    bm_start = sunrise_jd - 96/1440  # 96 minutes before sunrise
    return jd_to_local_time(bm_start, tz_offset), jd_to_local_time(bm_end, tz_offset)

def is_auspicious(jd: float) -> Tuple[bool, str]:
    """Check if the time is generally auspicious"""
    tithi_num, tithi_name, paksha = get_tithi(jd)
    yoga_num, yoga_name = get_yoga(jd)
    
    tithi_ok = tithi_num not in BAD_TITHI
    yoga_ok = yoga_name in GOOD_YOGA
    
    if tithi_ok and yoga_ok:
        return True, "Highly auspicious"
    elif tithi_ok or yoga_ok:
        return True, "Moderately auspicious"
    else:
        return False, "Avoid this time"

def get_full_panchang(target_date: date, lat: float, lon: float, tz_offset: float = 5.5) -> Dict:
    """Get complete panchang for a date"""
    dt = datetime(target_date.year, target_date.month, target_date.day, 6, 0, 0)
    jd = datetime_to_jd(dt, tz_offset)
    
    tithi_num, tithi_name, paksha = get_tithi(jd)
    yoga_num, yoga_name = get_yoga(jd)
    karana_num, karana_name = get_karana(jd)
    vara = get_vara(jd)
    masa = get_masa(jd)
    
    moon_lon = get_planet_lon(jd, swe.MOON)
    nakshatra, pada, deg = lon_to_nakshatra(moon_lon)
    moon_rashi, moon_deg = lon_to_rashi(moon_lon)
    
    sun_lon = get_planet_lon(jd, swe.SUN)
    sun_rashi, sun_deg = lon_to_rashi(sun_lon)
    
    sunrise_jd, sunset_jd = get_sunrise_sunset(jd, lat, lon)
    rk_start, rk_end = get_rahu_kaal(jd, lat, lon, tz_offset)
    gk_start, gk_end = get_gulika_kaal(jd, lat, lon, tz_offset)
    yg_start, yg_end = get_yamaganda(jd, lat, lon, tz_offset)
    ab_start, ab_end = get_abhijit_muhurta(jd, lat, lon, tz_offset)
    bm_start, bm_end = get_brahma_muhurta(jd, lat, lon, tz_offset)
    
    auspicious, auspicious_note = is_auspicious(jd)
    
    # Get all planet positions
    planets = {}
    for name, planet_id in PLANETS.items():
        p_lon = get_planet_lon(jd, planet_id if planet_id != -1 else swe.TRUE_NODE)
        if planet_id == -1:
            p_lon = (get_planet_lon(jd, swe.TRUE_NODE) + 180) % 360
        p_rashi, p_deg = lon_to_rashi(p_lon)
        p_nak, p_pada, _ = lon_to_nakshatra(p_lon)
        planets[name] = {
            'longitude': p_lon,
            'rashi': p_rashi,
            'degree': p_deg,
            'nakshatra': p_nak,
            'pada': p_pada
        }
    
    # Calculate Samvat
    samvat = target_date.year - 57 if target_date.month > 3 else target_date.year - 58
    
    return {
        'date': target_date,
        'samvat': samvat,
        'masa': masa,
        'paksha': paksha,
        'tithi': tithi_name,
        'tithi_num': tithi_num,
        'vara': vara,
        'nakshatra': nakshatra,
        'nakshatra_pada': pada,
        'moon_rashi': moon_rashi,
        'sun_rashi': sun_rashi,
        'yoga': yoga_name,
        'karana': karana_name,
        'sunrise': jd_to_local_time(sunrise_jd, tz_offset),
        'sunset': jd_to_local_time(sunset_jd, tz_offset),
        'rahu_kaal': (rk_start, rk_end),
        'gulika_kaal': (gk_start, gk_end),
        'yamaganda': (yg_start, yg_end),
        'abhijit_muhurta': (ab_start, ab_end),
        'brahma_muhurta': (bm_start, bm_end),
        'auspicious': auspicious,
        'auspicious_note': auspicious_note,
        'planets': planets,
        'moon_lon': moon_lon,
        'sun_lon': sun_lon,
    }

# ========== MARRIAGE MATCHING ENGINE ==========

NAKSHATRA_GANA = {
    "Ashwini": "Deva", "Bharani": "Manushya", "Krittika": "Rakshasa",
    "Rohini": "Manushya", "Mrigashira": "Deva", "Ardra": "Manushya",
    "Punarvasu": "Deva", "Pushya": "Deva", "Ashlesha": "Rakshasa",
    "Magha": "Rakshasa", "Purva Phalguni": "Manushya", "Uttara Phalguni": "Manushya",
    "Hasta": "Deva", "Chitra": "Rakshasa", "Swati": "Deva",
    "Vishakha": "Rakshasa", "Anuradha": "Deva", "Jyeshtha": "Rakshasa",
    "Mula": "Rakshasa", "Purva Ashadha": "Manushya", "Uttara Ashadha": "Manushya",
    "Shravana": "Deva", "Dhanishtha": "Rakshasa", "Shatabhisha": "Rakshasa",
    "Purva Bhadrapada": "Manushya", "Uttara Bhadrapada": "Manushya", "Revati": "Deva"
}

NAKSHATRA_NADI = {
    "Ashwini": "Aadi", "Bharani": "Madhya", "Krittika": "Antya",
    "Rohini": "Antya", "Mrigashira": "Madhya", "Ardra": "Aadi",
    "Punarvasu": "Aadi", "Pushya": "Madhya", "Ashlesha": "Antya",
    "Magha": "Antya", "Purva Phalguni": "Madhya", "Uttara Phalguni": "Aadi",
    "Hasta": "Aadi", "Chitra": "Madhya", "Swati": "Antya",
    "Vishakha": "Antya", "Anuradha": "Madhya", "Jyeshtha": "Aadi",
    "Mula": "Aadi", "Purva Ashadha": "Madhya", "Uttara Ashadha": "Antya",
    "Shravana": "Antya", "Dhanishtha": "Madhya", "Shatabhisha": "Aadi",
    "Purva Bhadrapada": "Aadi", "Uttara Bhadrapada": "Madhya", "Revati": "Antya"
}

NAKSHATRA_YONI = {
    "Ashwini": ("Horse", "M"), "Bharani": ("Elephant", "M"), "Krittika": ("Goat", "F"),
    "Rohini": ("Serpent", "M"), "Mrigashira": ("Serpent", "F"), "Ardra": ("Dog", "F"),
    "Punarvasu": ("Cat", "F"), "Pushya": ("Goat", "M"), "Ashlesha": ("Cat", "M"),
    "Magha": ("Rat", "M"), "Purva Phalguni": ("Rat", "F"), "Uttara Phalguni": ("Cow", "M"),
    "Hasta": ("Buffalo", "F"), "Chitra": ("Tiger", "F"), "Swati": ("Buffalo", "M"),
    "Vishakha": ("Tiger", "M"), "Anuradha": ("Deer", "F"), "Jyeshtha": ("Deer", "M"),
    "Mula": ("Dog", "M"), "Purva Ashadha": ("Monkey", "F"), "Uttara Ashadha": ("Mongoose", "M"),
    "Shravana": ("Monkey", "M"), "Dhanishtha": ("Lion", "F"), "Shatabhisha": ("Horse", "F"),
    "Purva Bhadrapada": ("Lion", "M"), "Uttara Bhadrapada": ("Cow", "F"), "Revati": ("Elephant", "F")
}

NAKSHATRA_RASHI = {
    "Ashwini": 0, "Bharani": 0, "Krittika": 0, "Rohini": 1, "Mrigashira": 1,
    "Ardra": 2, "Punarvasu": 2, "Pushya": 3, "Ashlesha": 3, "Magha": 4,
    "Purva Phalguni": 4, "Uttara Phalguni": 4, "Hasta": 5, "Chitra": 5,
    "Swati": 6, "Vishakha": 6, "Anuradha": 7, "Jyeshtha": 7, "Mula": 8,
    "Purva Ashadha": 8, "Uttara Ashadha": 8, "Shravana": 9, "Dhanishtha": 9,
    "Shatabhisha": 10, "Purva Bhadrapada": 10, "Uttara Bhadrapada": 11, "Revati": 11
}

RASHI_LORDS = {
    0: "Mars", 1: "Venus", 2: "Mercury", 3: "Moon", 4: "Sun",
    5: "Mercury", 6: "Venus", 7: "Mars", 8: "Jupiter", 9: "Saturn",
    10: "Saturn", 11: "Jupiter"
}

# Hostile yoni pairs
HOSTILE_YONI = {
    ("Cow", "Tiger"), ("Tiger", "Cow"), ("Elephant", "Lion"), ("Lion", "Elephant"),
    ("Horse", "Buffalo"), ("Buffalo", "Horse"), ("Dog", "Deer"), ("Deer", "Dog"),
    ("Rat", "Cat"), ("Cat", "Rat"), ("Mongoose", "Serpent"), ("Serpent", "Mongoose"),
    ("Goat", "Monkey"), ("Monkey", "Goat")
}

FRIENDLY_YONI = {
    ("Horse", "Horse"), ("Elephant", "Elephant"), ("Goat", "Goat"),
    ("Serpent", "Serpent"), ("Dog", "Dog"), ("Cat", "Cat"),
    ("Rat", "Rat"), ("Cow", "Cow"), ("Buffalo", "Buffalo"),
    ("Tiger", "Tiger"), ("Deer", "Deer"), ("Monkey", "Monkey"),
    ("Mongoose", "Mongoose"), ("Lion", "Lion")
}

def nakshatra_to_idx(name: str) -> int:
    return NAKSHATRA_NAMES.index(name)

def calc_varna(nakshatra: str) -> str:
    idx = nakshatra_to_idx(nakshatra)
    rashi = NAKSHATRA_RASHI[nakshatra]
    varnas = ["Shudra", "Vaishya", "Kshatriya", "Brahmin"]
    return varnas[rashi % 4]

def calc_vashya(rashi_idx: int) -> str:
    categories = {
        "Chatushpada": [0, 3, 8, 9],
        "Manava": [1, 2, 5, 6],
        "Jalchara": [3, 10, 11],
        "Vanachara": [4],
        "Keeta": [7]
    }
    for cat, rashis in categories.items():
        if rashi_idx in rashis:
            return cat
    return "Manava"

def calc_tara(boy_nak: str, girl_nak: str) -> Tuple[int, str]:
    b_idx = nakshatra_to_idx(boy_nak)
    g_idx = nakshatra_to_idx(girl_nak)
    tara_num = ((g_idx - b_idx) % 27) + 1
    tara_group = (tara_num - 1) % 9 + 1
    
    auspicious_taras = [1, 2, 4, 6, 8]
    inauspicious_taras = [3, 5, 7]
    
    if tara_group in auspicious_taras:
        return 3, "Auspicious"
    elif tara_group in inauspicious_taras:
        return 0, "Inauspicious"
    return 1, "Neutral"

def match_36_gunas(boy_nak: str, girl_nak: str, boy_gotra: str = "", girl_gotra: str = "") -> Dict:
    """Calculate 36 Gunas matching"""
    results = {}
    total = 0
    
    b_idx = nakshatra_to_idx(boy_nak)
    g_idx = nakshatra_to_idx(girl_nak)
    b_rashi = NAKSHATRA_RASHI[boy_nak]
    g_rashi = NAKSHATRA_RASHI[girl_nak]
    
    # 1. Varna (1 point)
    varna_order = ["Brahmin", "Kshatriya", "Vaishya", "Shudra"]
    b_varna = calc_varna(boy_nak)
    g_varna = calc_varna(girl_nak)
    b_varna_idx = varna_order.index(b_varna)
    g_varna_idx = varna_order.index(g_varna)
    varna_pts = 1 if b_varna_idx <= g_varna_idx else 0
    results['varna'] = {'points': varna_pts, 'max': 1, 'boy': b_varna, 'girl': g_varna,
                        'status': 'Compatible' if varna_pts == 1 else 'Incompatible'}
    total += varna_pts
    
    # 2. Vashya (2 points)
    b_vashya = calc_vashya(b_rashi)
    g_vashya = calc_vashya(g_rashi)
    vashya_pts = 2 if b_vashya == g_vashya else 1 if (
        (b_vashya == "Manava" and g_vashya == "Chatushpada") or
        (b_vashya == "Chatushpada" and g_vashya == "Manava")
    ) else 0
    results['vashya'] = {'points': vashya_pts, 'max': 2, 'boy': b_vashya, 'girl': g_vashya,
                         'status': 'Full' if vashya_pts == 2 else 'Partial' if vashya_pts == 1 else 'None'}
    total += vashya_pts
    
    # 3. Tara (3 points)
    tara_pts, tara_status = calc_tara(boy_nak, girl_nak)
    results['tara'] = {'points': tara_pts, 'max': 3, 'status': tara_status}
    total += tara_pts
    
    # 4. Yoni (4 points)
    b_yoni, b_yoni_gender = NAKSHATRA_YONI[boy_nak]
    g_yoni, g_yoni_gender = NAKSHATRA_YONI[girl_nak]
    
    if b_yoni == g_yoni:
        yoni_pts = 4
        yoni_status = "Excellent"
    elif (b_yoni, g_yoni) in HOSTILE_YONI:
        yoni_pts = 0
        yoni_status = "Hostile"
    else:
        yoni_pts = 2
        yoni_status = "Neutral"
    results['yoni'] = {'points': yoni_pts, 'max': 4, 'boy': f"{b_yoni} ({b_yoni_gender})", 
                       'girl': f"{g_yoni} ({g_yoni_gender})", 'status': yoni_status}
    total += yoni_pts
    
    # 5. Graha Maitri (5 points)
    b_lord = RASHI_LORDS[b_rashi]
    g_lord = RASHI_LORDS[g_rashi]
    
    planet_friends = {
        "Sun": ["Moon", "Mars", "Jupiter"], "Moon": ["Sun", "Mercury"],
        "Mars": ["Sun", "Moon", "Jupiter"], "Mercury": ["Sun", "Venus"],
        "Jupiter": ["Sun", "Moon", "Mars"], "Venus": ["Mercury", "Saturn"],
        "Saturn": ["Mercury", "Venus"]
    }
    
    b_friends = planet_friends.get(b_lord, [])
    g_friends = planet_friends.get(g_lord, [])
    
    if b_lord == g_lord:
        gm_pts = 5
        gm_status = "Same lord - Excellent"
    elif g_lord in b_friends and b_lord in g_friends:
        gm_pts = 5
        gm_status = "Mutual friends"
    elif g_lord in b_friends or b_lord in g_friends:
        gm_pts = 3
        gm_status = "One-sided friendship"
    else:
        gm_pts = 0
        gm_status = "Enemies"
    results['graha_maitri'] = {'points': gm_pts, 'max': 5, 'boy_lord': b_lord, 
                                'girl_lord': g_lord, 'status': gm_status}
    total += gm_pts
    
    # 6. Gana (6 points)
    b_gana = NAKSHATRA_GANA[boy_nak]
    g_gana = NAKSHATRA_GANA[girl_nak]
    
    gana_matrix = {
        ("Deva", "Deva"): 6, ("Manushya", "Manushya"): 6, ("Rakshasa", "Rakshasa"): 6,
        ("Deva", "Manushya"): 5, ("Manushya", "Deva"): 5,
        ("Manushya", "Rakshasa"): 1, ("Rakshasa", "Manushya"): 1,
        ("Deva", "Rakshasa"): 0, ("Rakshasa", "Deva"): 0
    }
    gana_pts = gana_matrix.get((b_gana, g_gana), 0)
    results['gana'] = {'points': gana_pts, 'max': 6, 'boy': b_gana, 'girl': g_gana,
                       'status': 'Excellent' if gana_pts == 6 else 'Good' if gana_pts >= 5 else 'Average' if gana_pts >= 3 else 'Poor'}
    total += gana_pts
    
    # 7. Bhakoot (7 points)
    nak_diff = (g_idx - b_idx) % 27
    rashi_diff = (g_rashi - b_rashi) % 12
    
    bad_bhakoot = [6, 8, 12, 2, 9, 5]  # 6/8, 2/12, 9/5 are inauspicious
    if rashi_diff in [0, 1, 3, 4, 6, 7, 10, 11]:
        bhakoot_pts = 7
        bhakoot_status = "Auspicious"
    else:
        bhakoot_pts = 0
        bhakoot_status = "Inauspicious (Dosha)"
    results['bhakoot'] = {'points': bhakoot_pts, 'max': 7, 
                           'rashi_diff': rashi_diff, 'status': bhakoot_status}
    total += bhakoot_pts
    
    # 8. Nadi (8 points)
    b_nadi = NAKSHATRA_NADI[boy_nak]
    g_nadi = NAKSHATRA_NADI[girl_nak]
    nadi_pts = 0 if b_nadi == g_nadi else 8
    nadi_status = "Nadi Dosha!" if b_nadi == g_nadi else "Compatible"
    results['nadi'] = {'points': nadi_pts, 'max': 8, 'boy': b_nadi, 'girl': g_nadi,
                       'status': nadi_status}
    total += nadi_pts
    
    # Gotra check
    gotra_ok = True
    gotra_note = ""
    if boy_gotra and girl_gotra:
        gotra_ok = boy_gotra.lower() != girl_gotra.lower()
        gotra_note = "✓ Different Gotras - Compatible" if gotra_ok else "⚠ Same Gotra - Marriage not recommended"
    
    return {
        'total': total,
        'max': 36,
        'percentage': (total / 36) * 100,
        'details': results,
        'gotra_compatible': gotra_ok,
        'gotra_note': gotra_note,
        'recommendation': get_matching_recommendation(total)
    }

def get_matching_recommendation(total: int) -> str:
    if total >= 32:
        return "Excellent Match - Highly Recommended"
    elif total >= 27:
        return "Very Good Match - Recommended"
    elif total >= 20:
        return "Good Match - Acceptable"
    elif total >= 18:
        return "Average Match - Proceed with care"
    else:
        return "Poor Match - Not Recommended"

def check_mangalik(birth_date: date, birth_lat: float, birth_lon: float, 
                   birth_time_h: int = 6, birth_time_m: int = 0, tz_offset: float = 5.5) -> Dict:
    """Check Mangalik status from D1, Moon chart, and D9"""
    dt = datetime(birth_date.year, birth_date.month, birth_date.day, birth_time_h, birth_time_m, 0)
    jd = datetime_to_jd(dt, tz_offset)
    
    # Get all planet positions
    planet_lons = {}
    for name, pid in PLANETS.items():
        if pid == -1:
            planet_lons[name] = (get_planet_lon(jd, swe.TRUE_NODE) + 180) % 360
        else:
            planet_lons[name] = get_planet_lon(jd, pid)
    
    # Calculate Lagna (Ascendant)
    ayanamsa = get_ayanamsa(jd)
    houses = swe.houses(jd, birth_lat, birth_lon, b'P')
    asc_lon = (houses[1][0] - ayanamsa) % 360
    
    def get_house_from_asc(planet_lon: float, asc_lon: float) -> int:
        diff = (planet_lon - asc_lon) % 360
        return int(diff / 30) + 1
    
    # D1 chart - Mars position
    mars_lon = planet_lons['Mars']
    mars_house_d1 = get_house_from_asc(mars_lon, asc_lon)
    
    # Moon chart - count from Moon as lagna
    moon_lon = planet_lons['Moon']
    mars_house_moon = get_house_from_asc(mars_lon, moon_lon)
    
    # D9 (Navamsha) - 9th harmonic
    def get_navamsha_lon(lon: float) -> float:
        rashi_lon = lon % 30
        navamsha_num = int(rashi_lon / (30/9))
        rashi_idx = int(lon / 30)
        fire_signs = [0, 4, 8]
        earth_signs = [1, 5, 9]
        air_signs = [2, 6, 10]
        water_signs = [3, 7, 11]
        
        if rashi_idx in fire_signs:
            start_rashi = 0
        elif rashi_idx in earth_signs:
            start_rashi = 9
        elif rashi_idx in air_signs:
            start_rashi = 6
        else:
            start_rashi = 3
        
        return ((start_rashi + navamsha_num) % 12) * 30 + 15
    
    mars_d9_lon = get_navamsha_lon(mars_lon)
    asc_d9_lon = get_navamsha_lon(asc_lon)
    mars_house_d9 = get_house_from_asc(mars_d9_lon, asc_d9_lon)
    
    # Mangalik houses: 1, 2, 4, 7, 8, 12
    mangalik_houses = [1, 2, 4, 7, 8, 12]
    
    d1_mangalik = mars_house_d1 in mangalik_houses
    moon_mangalik = mars_house_moon in mangalik_houses
    d9_mangalik = mars_house_d9 in mangalik_houses
    
    mangalik_count = sum([d1_mangalik, moon_mangalik, d9_mangalik])
    
    # Overall determination
    if mangalik_count >= 2:
        is_mangalik = True
        severity = "Strong Mangalik" if mangalik_count == 3 else "Mangalik"
    elif mangalik_count == 1:
        is_mangalik = True
        severity = "Mild Mangalik"
    else:
        is_mangalik = False
        severity = "Non-Mangalik"
    
    # Cancellation checks
    cancellations = []
    if mars_house_d1 in [1, 8] and int(asc_lon/30) in [0, 7]:  # Aries/Scorpio asc
        cancellations.append("Mars in own sign - reduces effect")
    if mars_house_d1 == 10:  # Mars in 10th in some traditions
        cancellations.append("Mars in 10th - partial cancellation")
    
    return {
        'is_mangalik': is_mangalik,
        'severity': severity,
        'mangalik_count': mangalik_count,
        'd1_mangalik': d1_mangalik,
        'd1_house': mars_house_d1,
        'moon_chart_mangalik': moon_mangalik,
        'moon_chart_house': mars_house_moon,
        'd9_mangalik': d9_mangalik,
        'd9_house': mars_house_d9,
        'cancellations': cancellations,
        'asc_lon': asc_lon,
        'asc_rashi': RASHI_NAMES[int(asc_lon/30)],
        'moon_rashi': RASHI_NAMES[int(moon_lon/30)],
        'planet_positions': {name: int(lon/30) for name, lon in planet_lons.items()}
    }

def get_nakshatra_from_dob(birth_date: date, birth_lat: float, birth_lon: float,
                            birth_time_h: int = 6, birth_time_m: int = 0, tz_offset: float = 5.5) -> Dict:
    """Get nakshatra and chart details from date of birth"""
    dt = datetime(birth_date.year, birth_date.month, birth_date.day, birth_time_h, birth_time_m, 0)
    jd = datetime_to_jd(dt, tz_offset)
    
    moon_lon = get_planet_lon(jd, swe.MOON)
    nakshatra, pada, deg = lon_to_nakshatra(moon_lon)
    moon_rashi, moon_deg = lon_to_rashi(moon_lon)
    
    sun_lon = get_planet_lon(jd, swe.SUN)
    sun_rashi, sun_deg = lon_to_rashi(sun_lon)
    
    # Lagna
    ayanamsa = get_ayanamsa(jd)
    try:
        houses = swe.houses(jd, birth_lat, birth_lon, b'P')
        asc_lon = (houses[1][0] - ayanamsa) % 360
    except:
        asc_lon = sun_lon  # fallback
    asc_rashi, asc_deg = lon_to_rashi(asc_lon)
    
    return {
        'nakshatra': nakshatra,
        'pada': pada,
        'moon_rashi': moon_rashi,
        'sun_rashi': sun_rashi,
        'lagna_rashi': asc_rashi,
        'lagna_lon': asc_lon,
        'moon_lon': moon_lon,
        'sun_lon': sun_lon,
    }

