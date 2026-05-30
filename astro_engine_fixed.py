import swisseph as swe
from datetime import datetime, date, timedelta
from functools import lru_cache
from zoneinfo import ZoneInfo

from timezonefinder import TimezoneFinder
from typing import Tuple, Dict

# Set ephemeris path
swe.set_ephe_path('')
tf = TimezoneFinder()


# ---------------------------------------------------------------------------
# TIMEZONE HELPERS
# ---------------------------------------------------------------------------

@lru_cache(maxsize=256)
def get_timezone(lat: float, lon: float):
    try:
        tz_name = tf.timezone_at(lat=lat, lng=lon)
        return ZoneInfo(tz_name if tz_name else "Asia/Kolkata")
    except Exception:
        return ZoneInfo("Asia/Kolkata")


def get_tz_offset_hours(dt: datetime, lat: float, lon: float) -> float:
    tz = get_timezone(lat, lon)
    local_dt = dt.replace(tzinfo=tz)
    return local_dt.utcoffset().total_seconds() / 3600.0


# ---------------------------------------------------------------------------
# LOOKUP TABLES
# ---------------------------------------------------------------------------

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

RASHI_HINDI = [
    "मेष", "वृषभ", "मिथुन", "कर्क", "सिंह", "कन्या",
    "तुला", "वृश्चिक", "धनु", "मकर", "कुम्भ", "मीन"
]

NAKSHATRA_HINDI = [
    "अश्विनी", "भरणी", "कृत्तिका", "रोहिणी", "मृगशिरा",
    "आर्द्रा", "पुनर्वसु", "पुष्य", "आश्लेषा", "मघा",
    "पूर्व फाल्गुनी", "उत्तर फाल्गुनी", "हस्त", "चित्रा", "स्वाति",
    "विशाखा", "अनुराधा", "ज्येष्ठा", "मूल", "पूर्वाषाढ़ा",
    "उत्तराषाढ़ा", "श्रवण", "धनिष्ठा", "शतभिषा",
    "पूर्व भाद्रपद", "उत्तर भाद्रपद", "रेवती"
]

GOOD_YOGA = frozenset(["Priti", "Ayushman", "Saubhagya", "Shobhana", "Sukarma", "Dhriti",
                       "Vriddhi", "Dhruva", "Harshana", "Siddhi", "Siddha", "Sadhya",
                       "Shubha", "Shukla", "Brahma", "Indra"])

BAD_YOGA = frozenset(["Vishkambha", "Atiganda", "Shula", "Ganda", "Vajra",
                      "Vyatipata", "Parigha", "Vaidhriti", "Vyaghata"])

GOOD_TITHI = frozenset([1, 2, 3, 5, 7, 10, 11, 13])
BAD_TITHI  = frozenset([4, 8, 9, 14, 15, 19, 23, 28, 29, 30])

# Rahu Kaal / Gulika / Yamaganda: 0-based slot index (0=first 1/8 of day) per weekday (0=Sun…6=Sat)
RAHU_KAAL   = {0: 7, 1: 1, 2: 6, 3: 4, 4: 5, 5: 3, 6: 2}
GULIKA_KAAL = {0: 6, 1: 5, 2: 4, 3: 3, 4: 2, 5: 1, 6: 7}
YAMAGANDA   = {0: 4, 1: 3, 2: 2, 3: 1, 4: 0, 5: 6, 6: 5}


# ---------------------------------------------------------------------------
# JULIAN DAY & AYANAMSA
# ---------------------------------------------------------------------------

def datetime_to_jd(dt: datetime, lat: float, lon: float) -> float:
    """Convert a naive local datetime to Julian Day (UT) using the IANA timezone
    for the given coordinates.  Uses timezone-aware conversion so DST and
    sub-hour offsets (e.g. IST +5:30) are handled exactly."""
    tz = get_timezone(lat, lon)
    local_dt = dt.replace(tzinfo=tz)
    utc_dt   = local_dt.astimezone(ZoneInfo("UTC"))
    hour_frac = (utc_dt.hour
                 + utc_dt.minute  / 60.0
                 + utc_dt.second  / 3600.0
                 + utc_dt.microsecond / 3_600_000_000.0)
    return swe.julday(utc_dt.year, utc_dt.month, utc_dt.day, hour_frac)


def parse_birth_time(time_input) -> Tuple[int, int, int]:
    """Parse birth time from multiple input formats into (hour, minute, second).

    Accepts:
      - "HH:MM"          -> (HH, MM, 0)
      - "HH:MM:SS"       -> (HH, MM, SS)
      - "HH:MM AM/PM"    -> converted to 24h
      - (h, m)           -> (h, m, 0)
      - (h, m, s)        -> (h, m, s)
      - int / float h    -> treated as decimal hours, e.g. 14.75 = 14:45:00
    This ensures no silent 15-minute rounding from the caller side.
    """
    if isinstance(time_input, str):
        time_input = time_input.strip().upper()
        ampm = None
        if time_input.endswith("AM") or time_input.endswith("PM"):
            ampm = time_input[-2:]
            time_input = time_input[:-2].strip()
        parts = time_input.split(":")
        h = int(parts[0])
        m = int(parts[1]) if len(parts) > 1 else 0
        s = int(parts[2]) if len(parts) > 2 else 0
        if ampm == "PM" and h != 12:
            h += 12
        elif ampm == "AM" and h == 12:
            h = 0
        return h, m, s
    if isinstance(time_input, (list, tuple)):
        parts = list(time_input)
        h = int(parts[0]) if len(parts) > 0 else 0
        m = int(parts[1]) if len(parts) > 1 else 0
        s = int(parts[2]) if len(parts) > 2 else 0
        return h, m, s
    if isinstance(time_input, float):
        # decimal hours: 14.75 → 14h 45m 0s
        h   = int(time_input)
        rem = (time_input - h) * 60.0
        m   = int(rem)
        s   = int(round((rem - m) * 60.0))
        return h, m, s
    return int(time_input), 0, 0


@lru_cache(maxsize=512)
def _ayanamsa_cached(jd: float) -> float:
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    return swe.get_ayanamsa(jd)


def get_ayanamsa(jd: float) -> float:
    """Lahiri (Chitrapaksha) ayanamsa for the given UT Julian Day."""
    return _ayanamsa_cached(jd)


# ---------------------------------------------------------------------------
# PLANET POSITIONS  (sidereal, Lahiri)
# ---------------------------------------------------------------------------

def get_planet_lon(jd: float, planet: int) -> float:
    """Return sidereal ecliptic longitude in [0, 360) using Lahiri ayanamsa.

    pyswisseph canonical pattern:
      swe.calc_ut(jd, body)[0]  →  (lon, lat, dist, speed_lon, speed_lat, speed_dist)
    Tropical lon is [0] of that tuple; subtract ayanamsa for sidereal.
    planet == -1 means Ketu (= Rahu + 180°).
    """
    ayanamsa = _ayanamsa_cached(jd)
    if planet == -1:
        rahu_trop = swe.calc_ut(jd, swe.TRUE_NODE)[0][0]
        return (rahu_trop - ayanamsa + 180.0) % 360.0
    trop_lon = swe.calc_ut(jd, planet)[0][0]
    return (trop_lon - ayanamsa) % 360.0


def get_sidereal_asc(jd: float, lat: float, lon: float) -> float:
    """Sidereal ascendant (Lagna) using Placidus house system."""
    ayanamsa = _ayanamsa_cached(jd)
    houses   = swe.houses(jd, lat, lon, b'P')   # returns (cusps, ascmc)
    trop_asc = houses[1][0]                      # ascmc[0] = tropical ASC
    return (trop_asc - ayanamsa) % 360.0


# ---------------------------------------------------------------------------
# NAKSHATRA / RASHI CONVERSIONS
# ---------------------------------------------------------------------------

# Each nakshatra = 360/27 = 13°20'.  Each pada = 360/108 = 3°20'.
_NAK_SPAN  = 360.0 / 27.0    # 13.3333...°
_PADA_SPAN = _NAK_SPAN / 4.0  # 3.3333...°


def lon_to_nakshatra(lon: float) -> Tuple[str, int, float]:
    """Convert sidereal longitude → (nakshatra_name, pada 1-4, degrees_in_nakshatra).

    Arithmetic is done on the integer arc-second value to avoid floating-point
    boundary errors near nakshatra transitions.
    """
    lon = lon % 360.0
    # Work in arc-seconds for integer precision
    lon_as  = int(round(lon * 3600.0))          # total arc-seconds
    nak_as  = int(round(_NAK_SPAN * 3600.0))     # arc-seconds per nakshatra (48000)
    pada_as = nak_as // 4                        # arc-seconds per pada      (12000)

    nak_idx  = lon_as // nak_as
    nak_idx  = min(nak_idx, 26)
    rem_as   = lon_as - nak_idx * nak_as
    pada     = rem_as // pada_as + 1
    pada     = min(int(pada), 4)
    deg_in_nak = rem_as / 3600.0

    return NAKSHATRA_NAMES[nak_idx], pada, deg_in_nak


def lon_to_rashi(lon: float) -> Tuple[str, float]:
    """Convert sidereal longitude → (rashi_name, degrees_in_rashi)."""
    lon = lon % 360.0
    idx = int(lon / 30.0)
    idx = min(idx, 11)
    return RASHI_NAMES[idx], lon - idx * 30.0


# ---------------------------------------------------------------------------
# PANCHANG ELEMENTS
# ---------------------------------------------------------------------------

def get_tithi(jd: float, sun_lon: float = None, moon_lon: float = None) -> Tuple[int, str, str]:
    if sun_lon is None:
        sun_lon = get_planet_lon(jd, swe.SUN)
    if moon_lon is None:
        moon_lon = get_planet_lon(jd, swe.MOON)
    diff      = (moon_lon - sun_lon) % 360.0
    tithi_num = min(int(diff / 12.0) + 1, 30)
    paksha    = "Shukla" if tithi_num <= 15 else "Krishna"
    tithi_name = TITHI_NAMES[tithi_num - 1]
    return tithi_num, tithi_name, paksha


def find_tithi_end(jd_start: float) -> float:
    """Binary-search tithi end time to ~1 second precision."""
    current_tithi = get_tithi(jd_start)[0]
    step = 1.0 / 24.0
    jd_lo, jd_hi = jd_start, jd_start + step
    for _ in range(72):
        if get_tithi(jd_hi)[0] != current_tithi:
            break
        jd_lo = jd_hi
        jd_hi += step
    else:
        return jd_hi
    while (jd_hi - jd_lo) > 1.0 / 86400.0:
        mid = (jd_lo + jd_hi) / 2.0
        if get_tithi(mid)[0] == current_tithi:
            jd_lo = mid
        else:
            jd_hi = mid
    return jd_hi


def find_nakshatra_end(jd_start: float) -> float:
    """Binary-search Moon nakshatra end time to ~1 second precision."""
    current_nak = lon_to_nakshatra(get_planet_lon(jd_start, swe.MOON))[0]
    step = 1.0 / 24.0
    jd_lo, jd_hi = jd_start, jd_start + step
    for _ in range(72):
        if lon_to_nakshatra(get_planet_lon(jd_hi, swe.MOON))[0] != current_nak:
            break
        jd_lo = jd_hi
        jd_hi += step
    else:
        return jd_hi
    while (jd_hi - jd_lo) > 1.0 / 86400.0:
        mid = (jd_lo + jd_hi) / 2.0
        if lon_to_nakshatra(get_planet_lon(mid, swe.MOON))[0] == current_nak:
            jd_lo = mid
        else:
            jd_hi = mid
    return jd_hi


def get_yoga(jd: float, sun_lon: float = None, moon_lon: float = None) -> Tuple[int, str]:
    if sun_lon is None:
        sun_lon = get_planet_lon(jd, swe.SUN)
    if moon_lon is None:
        moon_lon = get_planet_lon(jd, swe.MOON)
    yoga_lon = (sun_lon + moon_lon) % 360.0
    yoga_idx = min(int(yoga_lon / _NAK_SPAN), 26)
    return yoga_idx + 1, YOGA_NAMES[yoga_idx]


def get_karana(jd: float, sun_lon: float = None, moon_lon: float = None) -> Tuple[int, str]:
    if sun_lon is None:
        sun_lon = get_planet_lon(jd, swe.SUN)
    if moon_lon is None:
        moon_lon = get_planet_lon(jd, swe.MOON)
    diff     = (moon_lon - sun_lon) % 360.0
    karana_idx = int(diff / 6.0) % 11
    return karana_idx + 1, KARANA_NAMES[karana_idx]


def _find_next_amavasya(jd: float) -> float:
    """Return JD of the next Amavasya (tithi 30) that STARTS strictly after jd.

    Strategy:
    - Skip forward until we are past any tithi-30 that contains jd.
    - Step forward in 0.5-day increments (tithi 30 lasts ~23h so 0.5d steps
      guarantee we never skip over it).
    - Binary-search to the precise start of that tithi 30.
    """
    # If we are currently in tithi 30, skip past its end first
    if get_tithi(jd)[0] == 30:
        probe = jd + 0.5
        while get_tithi(probe)[0] == 30:
            probe += 0.5
        start = probe
    else:
        start = jd + 0.5

    probe = start
    for _ in range(70):           # up to 35 days in 0.5-day steps
        if get_tithi(probe)[0] == 30:
            # Binary-search back to the exact start of tithi-30
            lo, hi = probe - 0.6, probe
            # Ensure lo is before tithi 30
            while get_tithi(lo)[0] == 30:
                lo -= 0.5
            while (hi - lo) > 1.0 / 86400.0:
                mid = (lo + hi) / 2.0
                if get_tithi(mid)[0] == 30:
                    hi = mid
                else:
                    lo = mid
            return hi
        probe += 0.5
    return jd + 30.0          # fallback


def _find_prev_amavasya(jd: float) -> float:
    """Return JD of the start of the Amavasya (tithi 30) most recently before jd.
    Uses 0.5-day steps to avoid skipping short tithis."""
    if get_tithi(jd)[0] == 30:
        probe = jd - 0.5
        while get_tithi(probe)[0] == 30:
            probe -= 0.5
        start = probe
    else:
        start = jd - 0.5

    probe = start
    for _ in range(70):
        if get_tithi(probe)[0] == 30:
            lo, hi = probe - 0.6, probe
            while get_tithi(lo)[0] == 30:
                lo -= 0.5
            while (hi - lo) > 1.0 / 86400.0:
                mid = (lo + hi) / 2.0
                if get_tithi(mid)[0] == 30:
                    hi = mid
                else:
                    lo = mid
            return hi
        probe -= 0.5
    return jd - 30.0          # fallback


def _current_am_start(jd: float) -> float:
    """When called while inside tithi 30, binary-search the start of this Amavasya."""
    lo, hi = jd - 2.0, jd
    while get_tithi(lo)[0] == 30:
        lo -= 1.0
    while (hi - lo) > 1.0 / 86400.0:
        mid = (lo + hi) / 2.0
        if get_tithi(mid)[0] == 30:
            hi = mid
        else:
            lo = mid
    return hi


def get_masa(jd: float, sun_lon: float = None) -> str:  # sun_lon kept for API compat
    """Amāvasyānta lunar month name — named after Sun's rashi at the end Amavasya."""
    am_jd = _current_am_start(jd) if get_tithi(jd)[0] == 30 else _find_next_amavasya(jd)
    return MASA_NAMES[int(get_planet_lon(am_jd, swe.SUN) / 30.0) % 12]


def is_adhik_masa(jd: float, sun_lon: float = None) -> bool:  # sun_lon kept for API compat
    """True if current lunation is Adhika — Sun stays in same rashi at both Amavasyas."""
    end_am   = _current_am_start(jd) if get_tithi(jd)[0] == 30 else _find_next_amavasya(jd)
    start_am = _find_prev_amavasya(jd)
    return (int(get_planet_lon(start_am, swe.SUN) / 30.0) % 12 ==
            int(get_planet_lon(end_am,   swe.SUN) / 30.0) % 12)


def get_vara(jd: float, lat: float = 20.5937, lon: float = 78.9629) -> str:
    """Weekday (vara) from sunrise JD, resolved via actual local timezone."""
    dt_tuple = swe.revjul(jd)
    total_sec = round(dt_tuple[3] * 3600)
    h = (total_sec // 3600) % 24
    m = (total_sec % 3600) // 60
    s = total_sec % 60
    utc_dt = datetime(int(dt_tuple[0]), int(dt_tuple[1]), int(dt_tuple[2]),
                      int(h), int(m), int(s), tzinfo=ZoneInfo("UTC"))
    tz = get_timezone(lat, lon)
    local_dt  = utc_dt.astimezone(tz)
    python_wd = local_dt.weekday()       # 0=Mon … 6=Sun
    vedic_wd  = (python_wd + 1) % 7     # 0=Sun … 6=Sat
    return VARA_NAMES[vedic_wd]


# ---------------------------------------------------------------------------
# SUNRISE / SUNSET
# ---------------------------------------------------------------------------

@lru_cache(maxsize=512)
def get_sunrise_sunset(jd: float, lat: float, lon: float) -> Tuple[float, float]:
    """Precise Vedic sunrise/sunset via Swiss Ephemeris (upper limb, refraction)."""
    geopos = (lon, lat, 0)
    dt = swe.revjul(jd)
    # Use actual timezone offset for local midnight anchor
    _midnight_naive = datetime(int(dt[0]), int(dt[1]), int(dt[2]), 0, 0, 0)
    tz_actual = get_tz_offset_hours(_midnight_naive, lat, lon)
    jd_local_midnight = swe.julday(int(dt[0]), int(dt[1]), int(dt[2]), 0.0) - tz_actual / 24.0

    try:
        rise_result = swe.rise_trans(
            jd_local_midnight, swe.SUN, swe.CALC_RISE, geopos,
            atpress=1013.25, attemp=15.0
        )
        sunrise_jd = rise_result[1][0]
        set_result = swe.rise_trans(
            sunrise_jd + 0.1, swe.SUN, swe.CALC_SET, geopos,
            atpress=1013.25, attemp=15.0
        )
        sunset_jd = set_result[1][0]
        day_dur = (sunset_jd - sunrise_jd) * 24.0
        if not (6.0 <= day_dur <= 18.0):
            raise ValueError(f"Implausible day duration: {day_dur:.2f}h")
        return sunrise_jd, sunset_jd
    except Exception:
        tz_h = tz_actual
        return (jd - tz_h / 24.0 + 6.0 / 24.0,
                jd - tz_h / 24.0 + 18.0 / 24.0)


# ---------------------------------------------------------------------------
# TIME CONVERSION
# ---------------------------------------------------------------------------

def jd_to_local_time(jd: float, lat: float, lon: float, include_seconds: bool = False) -> str:
    """Convert Julian Day (UT) to local time string."""
    dt = swe.revjul(jd)
    total_seconds = round(dt[3] * 3600)
    h  = (total_seconds // 3600) % 24
    m  = (total_seconds % 3600) // 60
    s  = total_seconds % 60
    utc_dt = datetime(int(dt[0]), int(dt[1]), int(dt[2]),
                      int(h), int(m), int(s), tzinfo=ZoneInfo("UTC"))
    tz = get_timezone(lat, lon)
    local_dt = utc_dt.astimezone(tz)
    if include_seconds:
        return local_dt.strftime("%I:%M:%S %p")
    return local_dt.strftime("%I:%M %p")


# ---------------------------------------------------------------------------
# MUHURTA HELPERS
# ---------------------------------------------------------------------------

def _muhurta_slot(sunrise_jd: float, dur: float, slot: int,
                  lat: float, lon: float) -> Tuple[str, str]:
    start = sunrise_jd + slot * dur
    return (jd_to_local_time(start, lat, lon, True),
            jd_to_local_time(start + dur, lat, lon, True))


def get_rahu_kaal(sunrise_jd: float, sunset_jd: float, weekday: int,
                  lat: float, lon: float) -> Tuple[str, str]:
    return _muhurta_slot(sunrise_jd, (sunset_jd - sunrise_jd) / 8.0,
                         RAHU_KAAL[weekday], lat, lon)


def get_gulika_kaal(sunrise_jd: float, sunset_jd: float, weekday: int,
                    lat: float, lon: float) -> Tuple[str, str]:
    return _muhurta_slot(sunrise_jd, (sunset_jd - sunrise_jd) / 8.0,
                         GULIKA_KAAL[weekday], lat, lon)


def get_yamaganda(sunrise_jd: float, sunset_jd: float, weekday: int,
                  lat: float, lon: float) -> Tuple[str, str]:
    return _muhurta_slot(sunrise_jd, (sunset_jd - sunrise_jd) / 8.0,
                         YAMAGANDA[weekday], lat, lon)


def get_abhijit_muhurta(sunrise_jd: float, sunset_jd: float,
                        lat: float, lon: float) -> Tuple[str, str]:
    span    = sunset_jd - sunrise_jd
    muhurta = span / 15.0
    midday  = (sunrise_jd + sunset_jd) / 2.0
    return (jd_to_local_time(midday - muhurta / 2.0, lat, lon, True),
            jd_to_local_time(midday + muhurta / 2.0, lat, lon, True))


def get_brahma_muhurta(sunrise_jd: float, sunset_jd: float,
                       lat: float, lon: float) -> Tuple[str, str]:
    muhurta = (sunset_jd - sunrise_jd) / 15.0
    bm_start = sunrise_jd - 2.0 * muhurta
    return (jd_to_local_time(bm_start, lat, lon, True),
            jd_to_local_time(sunrise_jd, lat, lon, True))


def is_auspicious(jd: float, sun_lon: float = None, moon_lon: float = None) -> Tuple[bool, str]:
    tithi_num, _, _ = get_tithi(jd, sun_lon, moon_lon)
    _, yoga_name    = get_yoga(jd, sun_lon, moon_lon)
    tithi_ok = tithi_num not in BAD_TITHI
    yoga_ok  = yoga_name in GOOD_YOGA
    if tithi_ok and yoga_ok:
        return True, "Highly auspicious"
    elif tithi_ok or yoga_ok:
        return True, "Moderately auspicious"
    return False, "Avoid this time"


# ---------------------------------------------------------------------------
# FULL PANCHANG
# ---------------------------------------------------------------------------

@lru_cache(maxsize=256)
def get_full_panchang(target_date: date, lat: float, lon: float) -> Dict:
    """Complete panchang for a date at given coordinates."""
    dt_noon  = datetime(target_date.year, target_date.month, target_date.day, 12, 0, 0)
    jd_noon  = datetime_to_jd(dt_noon, lat, lon)
    sunrise_jd, sunset_jd = get_sunrise_sunset(jd_noon, lat, lon)
    jd = sunrise_jd   # panchang reference = sunrise

    # Pre-compute sun/moon once — reused by tithi, yoga, karana, masa, nakshatra
    sun_lon  = get_planet_lon(jd, swe.SUN)
    moon_lon = get_planet_lon(jd, swe.MOON)

    tithi_num, tithi_name, paksha = get_tithi(jd, sun_lon, moon_lon)
    _, yoga_name                  = get_yoga(jd, sun_lon, moon_lon)
    _, karana_name                = get_karana(jd, sun_lon, moon_lon)
    masa = get_masa(jd, sun_lon)

    nakshatra, pada, _deg = lon_to_nakshatra(moon_lon)
    moon_rashi, _         = lon_to_rashi(moon_lon)
    sun_rashi, _          = lon_to_rashi(sun_lon)

    tithi_end_jd = find_tithi_end(jd)
    nak_end_jd   = find_nakshatra_end(jd)

    # Weekday from local sunrise — shared with get_vara logic, computed once here
    _sr = swe.revjul(sunrise_jd)
    _ts = round(_sr[3] * 3600)
    _sr_utc = datetime(int(_sr[0]), int(_sr[1]), int(_sr[2]),
                       (_ts // 3600) % 24, (_ts % 3600) // 60,
                       _ts % 60, tzinfo=ZoneInfo("UTC"))
    _tz = get_timezone(lat, lon)
    _sr_local = _sr_utc.astimezone(_tz)
    python_wd = _sr_local.weekday()
    weekday   = (python_wd + 1) % 7
    vara      = VARA_NAMES[weekday]

    rk_start, rk_end = get_rahu_kaal(sunrise_jd, sunset_jd, weekday, lat, lon)
    gk_start, gk_end = get_gulika_kaal(sunrise_jd, sunset_jd, weekday, lat, lon)
    yg_start, yg_end = get_yamaganda(sunrise_jd, sunset_jd, weekday, lat, lon)
    ab_start, ab_end = get_abhijit_muhurta(sunrise_jd, sunset_jd, lat, lon)
    bm_start, bm_end = get_brahma_muhurta(sunrise_jd, sunset_jd, lat, lon)

    auspicious, auspicious_note = is_auspicious(jd, sun_lon, moon_lon)

    try:
        adhik = is_adhik_masa(jd, sun_lon)
    except Exception:
        adhik = False

    planets = {}
    for name, planet_id in PLANETS.items():
        p_lon = get_planet_lon(jd, planet_id)
        p_rashi, p_deg_in_rashi = lon_to_rashi(p_lon)
        p_nak, p_pada, p_nak_deg = lon_to_nakshatra(p_lon)
        rashi_idx = RASHI_NAMES.index(p_rashi)
        nak_idx   = NAKSHATRA_NAMES.index(p_nak)
        planets[name] = {
            'longitude':    round(p_lon, 4),       # full sidereal longitude
            'rashi':        p_rashi,
            'rashi_hi':     RASHI_HINDI[rashi_idx],
            'degree':       round(p_deg_in_rashi, 4),  # degrees within rashi
            'nakshatra':    p_nak,
            'nakshatra_hi': NAKSHATRA_HINDI[nak_idx],
            'pada':         p_pada,
            'nak_degree':   round(p_nak_deg, 4),   # degrees within nakshatra
        }

    samvat = target_date.year + 57 if target_date.month > 3 else target_date.year + 56

    return {
        'date': target_date,
        'samvat': samvat,
        'masa': masa,
        'is_adhik': adhik,
        'paksha': paksha,
        'tithi': tithi_name,
        'tithi_num': tithi_num,
        'tithi_end': jd_to_local_time(tithi_end_jd, lat, lon, True),
        'vara': vara,
        'nakshatra': nakshatra,
        'nakshatra_pada': pada,
        'nakshatra_end': jd_to_local_time(nak_end_jd, lat, lon, True),
        'moon_rashi': moon_rashi,
        'sun_rashi': sun_rashi,
        'yoga': yoga_name,
        'karana': karana_name,
        'sunrise': jd_to_local_time(sunrise_jd, lat, lon, True),
        'sunset': jd_to_local_time(sunset_jd, lat, lon, True),
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


# ---------------------------------------------------------------------------
# BIRTH PANCHANG  (janma kundali base — all at exact birth moment)
# ---------------------------------------------------------------------------

def get_birth_panchang(birth_date: date, birth_lat: float, birth_lon: float,
                       birth_time_h: int = 6, birth_time_m: int = 0,
                       birth_time_s: int = 0,
                       birth_time=None) -> Dict:
    """Complete panchang at the exact birth moment (h:m:s).
    Janma nakshatra and janma tithi are computed at the precise birth time —
    NOT at sunrise — which is the correct Vedic (Jyotisha) method.
    All end-times are found via binary search to ~1 second precision.

    birth_time (optional): accepts "HH:MM", "HH:MM:SS", "HH:MM AM/PM",
    a (h,m,s) tuple, or decimal hours float — overrides h/m/s integers.
    This eliminates any 15-minute rounding at the call site.
    """
    if birth_time is not None:
        birth_time_h, birth_time_m, birth_time_s = parse_birth_time(birth_time)
    dt = datetime(birth_date.year, birth_date.month, birth_date.day,
                  birth_time_h, birth_time_m, birth_time_s)
    jd = datetime_to_jd(dt, birth_lat, birth_lon)

    # Pre-compute sun/moon once — reused by tithi, yoga, karana, masa, nakshatra
    sun_lon  = get_planet_lon(jd, swe.SUN)
    moon_lon = get_planet_lon(jd, swe.MOON)

    nakshatra, pada, nak_deg = lon_to_nakshatra(moon_lon)
    moon_rashi, moon_deg     = lon_to_rashi(moon_lon)
    sun_rashi,  sun_deg      = lon_to_rashi(sun_lon)

    tithi_num, tithi_name, paksha = get_tithi(jd, sun_lon, moon_lon)
    _, yoga_name                  = get_yoga(jd, sun_lon, moon_lon)
    _, karana_name                = get_karana(jd, sun_lon, moon_lon)
    vara = get_vara(jd, birth_lat, birth_lon)
    masa = get_masa(jd, sun_lon)

    asc_lon = get_sidereal_asc(jd, birth_lat, birth_lon)
    asc_rashi, asc_deg = lon_to_rashi(asc_lon)

    tithi_end_jd = find_tithi_end(jd)
    nak_end_jd   = find_nakshatra_end(jd)

    planets = {}
    for name, planet_id in PLANETS.items():
        p_lon = get_planet_lon(jd, planet_id)
        p_rashi, p_deg = lon_to_rashi(p_lon)
        p_nak, p_pada, p_nak_deg = lon_to_nakshatra(p_lon)
        planets[name] = {
            'longitude':  round(p_lon, 6),
            'rashi':      p_rashi,
            'degree':     round(p_deg, 4),
            'nakshatra':  p_nak,
            'pada':       p_pada,
            'nak_degree': round(p_nak_deg, 4),
        }

    try:
        adhik = is_adhik_masa(jd, sun_lon)
    except Exception:
        adhik = False

    return {
        'birth_datetime':       dt.strftime("%Y-%m-%d %H:%M:%S"),
        'masa':                 masa,
        'is_adhik':             adhik,
        'paksha':               paksha,
        'vara':                 vara,
        'janma_tithi_num':      tithi_num,
        'janma_tithi':          tithi_name,
        'tithi_end':            jd_to_local_time(tithi_end_jd, birth_lat, birth_lon, True),
        'janma_nakshatra':      nakshatra,
        'janma_nakshatra_pada': pada,
        # Alias keys used by app_new.py
        'nakshatra':            nakshatra,
        'nakshatra_pada':       pada,
        'nakshatra_deg':        round(nak_deg, 4),
        'nakshatra_end':        jd_to_local_time(nak_end_jd, birth_lat, birth_lon, True),
        'moon_rashi':           moon_rashi,
        'moon_deg':             round(moon_deg, 4),
        'moon_lon':             round(moon_lon, 6),
        'sun_rashi':            sun_rashi,
        'sun_deg':              round(sun_deg, 4),
        'sun_lon':              round(sun_lon, 6),
        'lagna_rashi':          asc_rashi,
        'lagna_deg':            round(asc_deg, 4),
        'lagna_lon':            round(asc_lon, 6),
        'yoga':                 yoga_name,
        'karana':               karana_name,
        'planets':              planets,
    }


def get_nakshatra_from_dob(birth_date: date, birth_lat: float, birth_lon: float,
                            birth_time_h: int = 6, birth_time_m: int = 0,
                            birth_time_s: int = 0,
                            birth_time=None) -> Dict:
    """Return birth nakshatra, tithi and chart details.

    Preserves ALL original key names (nakshatra, pada, tithi, lagna_rashi ...)
    so existing app code does not break, while also including the verbose
    janma_* aliases used by get_birth_panchang.

    birth_time (optional): "HH:MM", "HH:MM:SS", "HH:MM AM/PM", (h,m,s) tuple,
    or decimal hours float — use this to pass exact minute:second from the UI
    and eliminate any 15-minute rounding.
    """
    if birth_time is not None:
        birth_time_h, birth_time_m, birth_time_s = parse_birth_time(birth_time)
    bp = get_birth_panchang(birth_date, birth_lat, birth_lon,
                            birth_time_h, birth_time_m, birth_time_s)

    result = dict(bp)
    # Backward-compatible short aliases that differ from the janma_* keys in bp
    result['nakshatra'] = bp['janma_nakshatra']
    result['pada']      = bp['janma_nakshatra_pada']
    result['tithi']     = bp['janma_tithi']
    result['tithi_num'] = bp['janma_tithi_num']
    return result


# ---------------------------------------------------------------------------
# MARRIAGE MATCHING (Ashtakoot / 36 Guna Milana)
# ---------------------------------------------------------------------------

# --- Nakshatra attribute tables (all 27) ---

# Gana: Deva / Manushya / Rakshasa
NAKSHATRA_GANA = {
    "Ashwini":          "Deva",     "Bharani":           "Manushya", "Krittika":          "Rakshasa",
    "Rohini":           "Manushya", "Mrigashira":        "Deva",     "Ardra":             "Manushya",
    "Punarvasu":        "Deva",     "Pushya":            "Deva",     "Ashlesha":          "Rakshasa",
    "Magha":            "Rakshasa", "Purva Phalguni":    "Manushya", "Uttara Phalguni":   "Manushya",
    "Hasta":            "Deva",     "Chitra":            "Rakshasa", "Swati":             "Deva",
    "Vishakha":         "Rakshasa", "Anuradha":          "Deva",     "Jyeshtha":          "Rakshasa",
    "Mula":             "Rakshasa", "Purva Ashadha":     "Manushya", "Uttara Ashadha":    "Manushya",
    "Shravana":         "Deva",     "Dhanishtha":        "Rakshasa", "Shatabhisha":       "Rakshasa",
    "Purva Bhadrapada": "Manushya", "Uttara Bhadrapada": "Manushya", "Revati":            "Deva",
}

# Nadi: Aadi / Madhya / Antya  (repeating cycle of 9 nakshatras each)
NAKSHATRA_NADI = {
    "Ashwini": "Aadi",  "Bharani": "Madhya",  "Krittika": "Antya",
    "Rohini":  "Antya", "Mrigashira": "Madhya","Ardra":  "Aadi",
    "Punarvasu":"Aadi", "Pushya": "Madhya",    "Ashlesha":"Antya",
    "Magha":   "Antya", "Purva Phalguni":"Madhya","Uttara Phalguni":"Aadi",
    "Hasta":   "Aadi",  "Chitra":"Madhya",     "Swati":   "Antya",
    "Vishakha":"Antya", "Anuradha":"Madhya",   "Jyeshtha":"Aadi",
    "Mula":    "Aadi",  "Purva Ashadha":"Madhya","Uttara Ashadha":"Antya",
    "Shravana":"Antya", "Dhanishtha":"Madhya", "Shatabhisha":"Aadi",
    "Purva Bhadrapada":"Aadi","Uttara Bhadrapada":"Madhya","Revati":"Antya",
}

# Yoni: animal symbol and gender
NAKSHATRA_YONI = {
    "Ashwini":          ("Horse",    "M"), "Bharani":           ("Elephant","M"),
    "Krittika":         ("Goat",     "F"), "Rohini":            ("Serpent", "M"),
    "Mrigashira":       ("Serpent",  "F"), "Ardra":             ("Dog",     "F"),
    "Punarvasu":        ("Cat",      "F"), "Pushya":            ("Goat",    "M"),
    "Ashlesha":         ("Cat",      "M"), "Magha":             ("Rat",     "M"),
    "Purva Phalguni":   ("Rat",      "F"), "Uttara Phalguni":   ("Cow",     "M"),
    "Hasta":            ("Buffalo",  "F"), "Chitra":            ("Tiger",   "F"),
    "Swati":            ("Buffalo",  "M"), "Vishakha":          ("Tiger",   "M"),
    "Anuradha":         ("Deer",     "F"), "Jyeshtha":          ("Deer",    "M"),
    "Mula":             ("Dog",      "M"), "Purva Ashadha":     ("Monkey",  "F"),
    "Uttara Ashadha":   ("Mongoose", "M"), "Shravana":          ("Monkey",  "M"),
    "Dhanishtha":       ("Lion",     "F"), "Shatabhisha":       ("Horse",   "F"),
    "Purva Bhadrapada": ("Lion",     "M"), "Uttara Bhadrapada": ("Cow",     "F"),
    "Revati":           ("Elephant", "F"),
}

# Rashi lord of each nakshatra's Moon sign  (corrected per classical Jyotisha)
# Krittika starts at 26°40' Mesha → the nakshatra belongs to VRISHABHA for guna purposes
# Uttara Phalguni starts at 26°40' Simha → belongs to KANYA
# Uttara Ashadha starts at 26°40' Dhanu → belongs to MAKARA
# Uttara Bhadrapada starts at 26°40' Kumbha → belongs to MEENA
NAKSHATRA_RASHI = {
    "Ashwini":          0,   # Mesha
    "Bharani":          0,   # Mesha
    "Krittika":         1,   # Vrishabha  ← corrected (not 0)
    "Rohini":           1,   # Vrishabha
    "Mrigashira":       2,   # Mithuna    (Mrigashira spans Vrishabha-Mithuna; Mithuna pada used)
    "Ardra":            2,   # Mithuna
    "Punarvasu":        3,   # Karka      (Punarvasu spans Mithuna-Karka; Karka pada used)
    "Pushya":           3,   # Karka
    "Ashlesha":         3,   # Karka
    "Magha":            4,   # Simha
    "Purva Phalguni":   4,   # Simha
    "Uttara Phalguni":  5,   # Kanya      ← corrected (not 4)
    "Hasta":            5,   # Kanya
    "Chitra":           6,   # Tula       (Chitra spans Kanya-Tula; Tula pada used)
    "Swati":            6,   # Tula
    "Vishakha":         7,   # Vrishchika (Vishakha spans Tula-Vrishchika; Vrishchika pada used)
    "Anuradha":         7,   # Vrishchika
    "Jyeshtha":         7,   # Vrishchika
    "Mula":             8,   # Dhanu
    "Purva Ashadha":    8,   # Dhanu
    "Uttara Ashadha":   9,   # Makara     ← corrected (not 8)
    "Shravana":         9,   # Makara
    "Dhanishtha":       10,  # Kumbha     (Dhanishtha spans Makara-Kumbha; Kumbha pada used)
    "Shatabhisha":      10,  # Kumbha
    "Purva Bhadrapada": 11,  # Meena      (PB spans Kumbha-Meena; Meena pada used)
    "Uttara Bhadrapada":11,  # Meena      ← corrected (not 10? already 11 — ok)
    "Revati":           11,  # Meena
}

# Rashi lords (classical Jyotisha — no outer planets)
RASHI_LORDS = {
    0: "Mars",    1: "Venus",   2: "Mercury", 3: "Moon",
    4: "Sun",     5: "Mercury", 6: "Venus",   7: "Mars",
    8: "Jupiter", 9: "Saturn",  10: "Saturn", 11: "Jupiter"
}

# Varna per nakshatra (classical assignment — NOT rashi % 4)
NAKSHATRA_VARNA = {
    "Ashwini":          "Vaishya",   "Bharani":           "Mleccha",
    "Krittika":         "Brahmin",   "Rohini":            "Shudra",
    "Mrigashira":       "Vaishya",   "Ardra":             "Mleccha",    # some texts: Shudra
    "Punarvasu":        "Vaishya",   "Pushya":            "Kshatriya",
    "Ashlesha":         "Mleccha",   "Magha":             "Shudra",
    "Purva Phalguni":   "Brahmin",   "Uttara Phalguni":   "Kshatriya",
    "Hasta":            "Vaishya",   "Chitra":            "Shudra",
    "Swati":            "Mleccha",   "Vishakha":          "Mleccha",
    "Anuradha":         "Shudra",    "Jyeshtha":          "Shudra",
    "Mula":             "Mleccha",   "Purva Ashadha":     "Brahmin",
    "Uttara Ashadha":   "Kshatriya", "Shravana":          "Mleccha",
    "Dhanishtha":       "Shudra",    "Shatabhisha":       "Vaishya",
    "Purva Bhadrapada": "Brahmin",   "Uttara Bhadrapada": "Kshatriya",
    "Revati":           "Brahmin",
}

# Hostile yoni pairs
HOSTILE_YONI = {
    ("Cow", "Tiger"), ("Tiger", "Cow"),
    ("Elephant", "Lion"), ("Lion", "Elephant"),
    ("Horse", "Buffalo"), ("Buffalo", "Horse"),
    ("Dog", "Deer"), ("Deer", "Dog"),
    ("Rat", "Cat"), ("Cat", "Rat"),
    ("Mongoose", "Serpent"), ("Serpent", "Mongoose"),
    ("Goat", "Monkey"), ("Monkey", "Goat"),
}

# Graha Maitri — classical natural friendship table
# friend / neutral / enemy for each graha
_GRAHA_FRIENDS  = {
    "Sun":     ["Moon", "Mars", "Jupiter"],
    "Moon":    ["Sun", "Mercury"],
    "Mars":    ["Sun", "Moon", "Jupiter"],
    "Mercury": ["Sun", "Venus"],
    "Jupiter": ["Sun", "Moon", "Mars"],
    "Venus":   ["Mercury", "Saturn"],
    "Saturn":  ["Mercury", "Venus"],
}
_GRAHA_ENEMIES  = {
    "Sun":     ["Venus", "Saturn"],
    "Moon":    ["None"],
    "Mars":    ["Mercury"],
    "Mercury": ["Moon"],
    "Jupiter": ["Mercury", "Venus"],
    "Venus":   ["Sun", "Moon"],
    "Saturn":  ["Sun", "Moon", "Mars"],
}


def _graha_relation(a: str, b: str) -> str:
    """Return 'friend', 'neutral', or 'enemy' from a's perspective of b."""
    if b in _GRAHA_FRIENDS.get(a, []):
        return "friend"
    if b in _GRAHA_ENEMIES.get(a, []):
        return "enemy"
    return "neutral"


_NAKSHATRA_IDX = {n: i for i, n in enumerate(NAKSHATRA_NAMES)}  # O(1) lookup

def nakshatra_to_idx(name: str) -> int:
    return _NAKSHATRA_IDX[name]


def calc_vashya(rashi_idx: int) -> str:
    """Vashya category per rashi index (0=Mesha … 11=Meena).
    Classical assignment — no overlap."""
    # Chatushpada: Mesha(0), Vrishabha(1), Simha(4), Dhanu(8) 1st half, Makara(9) 1st half
    # Manava:      Mithuna(2), Kanya(5), Tula(6), first half of Dhanu, Kumbha(10)
    # Jalchara:    Karka(3), Meena(11), Makara second half
    # Vanachara:   Simha(4) — some traditions
    # Keeta:       Vrishchika(7)
    # Simplified standard used in most matching software:
    vashya_map = {
        0: "Chatushpada",  # Mesha
        1: "Chatushpada",  # Vrishabha
        2: "Manava",       # Mithuna
        3: "Jalchara",     # Karka
        4: "Vanachara",    # Simha
        5: "Manava",       # Kanya
        6: "Manava",       # Tula
        7: "Keeta",        # Vrishchika
        8: "Chatushpada",  # Dhanu
        9: "Chatushpada",  # Makara
        10: "Manava",      # Kumbha
        11: "Jalchara",    # Meena
    }
    return vashya_map.get(rashi_idx, "Manava")


def calc_tara(boy_nak: str, girl_nak: str) -> Tuple[int, str]:
    """Tara (3 pts max).  Count girl's nakshatra from boy's; result mod 9.
    Taras 1,2,4,6,8 are auspicious (3 pts); 3,5,7 are inauspicious (0 pts)."""
    b_idx = nakshatra_to_idx(boy_nak)
    g_idx = nakshatra_to_idx(girl_nak)
    tara_num  = ((g_idx - b_idx) % 27) + 1
    tara_group = ((tara_num - 1) % 9) + 1   # 1…9
    if tara_group in [1, 2, 4, 6, 8]:
        return 3, "Auspicious"
    elif tara_group in [3, 5, 7]:
        return 0, "Inauspicious"
    return 1, "Neutral"


def match_36_gunas(boy_nak: str, girl_nak: str,
                   boy_gotra: str = "", girl_gotra: str = "") -> Dict:
    """Ashtakoot Guna Milana — 36 point compatibility calculation.

    All 8 kutas use the corrected classical tables:
      1. Varna   (1)  — per-nakshatra table, not rashi % 4
      2. Vashya  (2)  — corrected rashi→vashya map
      3. Tara    (3)  — count girl's nak from boy's, mod 9
      4. Yoni    (4)  — animal symbol compatibility
      5. Graha Maitri (5) — natural friendship, including neutral
      6. Gana    (6)  — Deva/Manushya/Rakshasa
      7. Bhakoot (7)  — rashi interval compatibility
      8. Nadi    (8)  — Aadi/Madhya/Antya
    """
    results = {}
    total   = 0

    b_rashi = NAKSHATRA_RASHI[boy_nak]
    g_rashi = NAKSHATRA_RASHI[girl_nak]

    # 1. Varna (1 point) — boy's varna must be >= girl's varna rank
    varna_order = ["Brahmin", "Kshatriya", "Vaishya", "Shudra", "Mleccha"]
    b_varna = NAKSHATRA_VARNA[boy_nak]
    g_varna = NAKSHATRA_VARNA[girl_nak]
    b_vi = varna_order.index(b_varna)
    g_vi = varna_order.index(g_varna)
    varna_pts = 1 if b_vi <= g_vi else 0
    results['varna'] = {'points': varna_pts, 'max': 1,
                        'boy': b_varna, 'girl': g_varna,
                        'status': 'Compatible' if varna_pts else 'Incompatible'}
    total += varna_pts

    # 2. Vashya (2 points)
    b_vashya = calc_vashya(b_rashi)
    g_vashya = calc_vashya(g_rashi)
    if b_vashya == g_vashya:
        vashya_pts, vashya_status = 2, "Full"
    elif ({b_vashya, g_vashya} == {"Manava", "Chatushpada"}
          or {b_vashya, g_vashya} == {"Manava", "Vanachara"}):
        vashya_pts, vashya_status = 1, "Partial"
    else:
        vashya_pts, vashya_status = 0, "None"
    results['vashya'] = {'points': vashya_pts, 'max': 2,
                         'boy': b_vashya, 'girl': g_vashya,
                         'status': vashya_status}
    total += vashya_pts

    # 3. Tara (3 points)
    tara_pts, tara_status = calc_tara(boy_nak, girl_nak)
    results['tara'] = {'points': tara_pts, 'max': 3, 'status': tara_status}
    total += tara_pts

    # 4. Yoni (4 points)
    b_yoni, b_ygender = NAKSHATRA_YONI[boy_nak]
    g_yoni, g_ygender = NAKSHATRA_YONI[girl_nak]
    if b_yoni == g_yoni and b_ygender != g_ygender:
        yoni_pts, yoni_status = 4, "Excellent (same animal, opposite gender)"
    elif b_yoni == g_yoni:
        yoni_pts, yoni_status = 3, "Good (same animal)"
    elif (b_yoni, g_yoni) in HOSTILE_YONI:
        yoni_pts, yoni_status = 0, "Hostile"
    else:
        yoni_pts, yoni_status = 2, "Neutral"
    results['yoni'] = {'points': yoni_pts, 'max': 4,
                       'boy': f"{b_yoni} ({b_ygender})",
                       'girl': f"{g_yoni} ({g_ygender})",
                       'status': yoni_status}
    total += yoni_pts

    # 5. Graha Maitri (5 points) — uses natural friendship + neutral
    b_lord = RASHI_LORDS[b_rashi]
    g_lord = RASHI_LORDS[g_rashi]
    b_rel = _graha_relation(b_lord, g_lord)   # b_lord's view of g_lord
    g_rel = _graha_relation(g_lord, b_lord)   # g_lord's view of b_lord

    if b_lord == g_lord:
        gm_pts, gm_status = 5, "Same lord"
    elif b_rel == "friend" and g_rel == "friend":
        gm_pts, gm_status = 5, "Mutual friends"
    elif b_rel == "friend" and g_rel == "neutral":
        gm_pts, gm_status = 4, "Friend + Neutral"
    elif b_rel == "neutral" and g_rel == "friend":
        gm_pts, gm_status = 4, "Neutral + Friend"
    elif b_rel == "neutral" and g_rel == "neutral":
        gm_pts, gm_status = 3, "Mutual neutral"
    elif b_rel == "friend" and g_rel == "enemy":
        gm_pts, gm_status = 1, "Friend + Enemy"
    elif b_rel == "enemy" and g_rel == "friend":
        gm_pts, gm_status = 1, "Enemy + Friend"
    elif b_rel == "neutral" and g_rel == "enemy":
        gm_pts, gm_status = 1, "Neutral + Enemy"
    elif b_rel == "enemy" and g_rel == "neutral":
        gm_pts, gm_status = 1, "Enemy + Neutral"
    else:
        gm_pts, gm_status = 0, "Mutual enemies"
    results['graha_maitri'] = {'points': gm_pts, 'max': 5,
                                'boy_lord': b_lord, 'girl_lord': g_lord,
                                'status': gm_status}
    total += gm_pts

    # 6. Gana (6 points)
    b_gana = NAKSHATRA_GANA[boy_nak]
    g_gana = NAKSHATRA_GANA[girl_nak]
    gana_matrix = {
        ("Deva",     "Deva"):     6,
        ("Manushya", "Manushya"): 6,
        ("Rakshasa", "Rakshasa"): 6,
        ("Deva",     "Manushya"): 5,
        ("Manushya", "Deva"):     5,
        ("Manushya", "Rakshasa"): 1,
        ("Rakshasa", "Manushya"): 1,
        ("Deva",     "Rakshasa"): 0,
        ("Rakshasa", "Deva"):     0,
    }
    gana_pts = gana_matrix.get((b_gana, g_gana), 0)
    results['gana'] = {'points': gana_pts, 'max': 6,
                       'boy': b_gana, 'girl': g_gana,
                       'status': ('Excellent' if gana_pts == 6 else
                                  'Good'      if gana_pts >= 5 else
                                  'Average'   if gana_pts >= 3 else 'Poor')}
    total += gana_pts

    # 7. Bhakoot (7 points)
    rashi_diff = (g_rashi - b_rashi) % 12
    # Inauspicious intervals: 6/8, 2/12, 9/5 (from boy to girl)
    inauspicious = {2, 6, 8, 12}   # if rashi_diff in these → 0 pts
    # Also check reverse: (b_rashi - g_rashi) % 12
    rev_diff = (b_rashi - g_rashi) % 12
    if rashi_diff in inauspicious or rev_diff in inauspicious:
        bhakoot_pts, bhakoot_status = 0, "Inauspicious (Dosha)"
    else:
        bhakoot_pts, bhakoot_status = 7, "Auspicious"
    results['bhakoot'] = {'points': bhakoot_pts, 'max': 7,
                           'rashi_diff': rashi_diff,
                           'status': bhakoot_status}
    total += bhakoot_pts

    # 8. Nadi (8 points)
    b_nadi = NAKSHATRA_NADI[boy_nak]
    g_nadi = NAKSHATRA_NADI[girl_nak]
    nadi_pts    = 0 if b_nadi == g_nadi else 8
    nadi_status = "Nadi Dosha!" if b_nadi == g_nadi else "Compatible"
    results['nadi'] = {'points': nadi_pts, 'max': 8,
                       'boy': b_nadi, 'girl': g_nadi,
                       'status': nadi_status}
    total += nadi_pts

    # Gotra check (not a kuta, informational only)
    gotra_ok   = True
    gotra_note = ""
    if boy_gotra and girl_gotra:
        gotra_ok   = boy_gotra.strip().lower() != girl_gotra.strip().lower()
        gotra_note = (" Different Gotras - Compatible" if gotra_ok
                      else " Same Gotra - Marriage not recommended")

    return {
        'total':          total,
        'max':            36,
        'percentage':     round((total / 36) * 100, 1),
        'details':        results,
        'gotra_compatible': gotra_ok,
        'gotra_note':     gotra_note,
        'recommendation': _matching_recommendation(total),
    }


def _matching_recommendation(total: int) -> str:
    if total >= 32: return "Excellent Match - Highly Recommended"
    if total >= 27: return "Very Good Match - Recommended"
    if total >= 20: return "Good Match - Acceptable"
    if total >= 18: return "Average Match - Proceed with care"
    return "Poor Match - Not Recommended"

# keep old name working
get_matching_recommendation = _matching_recommendation


# ---------------------------------------------------------------------------
# MANGALIK CHECK
# ---------------------------------------------------------------------------

def _navamsha_rashi(lon: float) -> int:
    """Return the Navamsha rashi index (0-11) for a given sidereal longitude.

    Formula (classical):
      - Determine the rashi (0-11) and degrees within that rashi.
      - Navamsha number within the rashi = floor(deg_in_rashi / (30/9)) = floor(deg/3.333)
      - Starting navamsha rashi depends on the element of the natal rashi:
          Fire (Mesha 0, Simha 4, Dhanu 8)  → starts from Mesha   (0)
          Earth(Vrishabha1,Kanya5,Makara9)  → starts from Makara  (9)
          Air  (Mithuna2,Tula6,Kumbha10)    → starts from Tula    (6)
          Water(Karka3,Vrishchika7,Meena11) → starts from Karka   (3)
    """
    lon       = lon % 360.0
    rashi_idx = int(lon / 30.0)
    deg_in_r  = lon - rashi_idx * 30.0
    nav_num   = int(deg_in_r / (30.0 / 9.0))   # 0..8

    start = {0: 0, 4: 0, 8: 0,    # Fire  → Mesha
             1: 9, 5: 9, 9: 9,    # Earth → Makara
             2: 6, 6: 6, 10: 6,   # Air   → Tula
             3: 3, 7: 3, 11: 3,   # Water → Karka
             }[rashi_idx]
    return (start + nav_num) % 12


def check_mangalik(birth_date: date, birth_lat: float, birth_lon: float,
                   birth_time_h: int = 6, birth_time_m: int = 0,
                   birth_time_s: int = 0,
                   birth_time=None) -> Dict:
    """Mangalik dosha check from D1, Moon chart, and D9 (Navamsha).

    Classical Mangalik houses: 1, 2, 4, 7, 8, 12.
    House placement uses whole-sign counting from Lagna / Moon / D9-Lagna.

    birth_time (optional): "HH:MM", "HH:MM:SS", (h,m,s) tuple, or decimal hours
    — overrides birth_time_h/m/s integers.
    """
    if birth_time is not None:
        birth_time_h, birth_time_m, birth_time_s = parse_birth_time(birth_time)
    dt = datetime(birth_date.year, birth_date.month, birth_date.day,
                  birth_time_h, birth_time_m, birth_time_s)
    jd = datetime_to_jd(dt, birth_lat, birth_lon)

    # All sidereal planet longitudes
    planet_lons = {name: get_planet_lon(jd, pid) for name, pid in PLANETS.items()}

    # Sidereal ascendant
    asc_lon = get_sidereal_asc(jd, birth_lat, birth_lon)

    def whole_sign_house(planet_lon: float, lagna_lon: float) -> int:
        """Whole-sign house number (1-12) of planet from lagna."""
        lagna_rashi = int(lagna_lon / 30.0)
        planet_rashi = int(planet_lon / 30.0)
        return (planet_rashi - lagna_rashi) % 12 + 1

    mars_lon = planet_lons['Mars']
    moon_lon = planet_lons['Moon']

    # D1 — from Lagna
    mars_house_d1 = whole_sign_house(mars_lon, asc_lon)

    # Moon chart — from Moon as Lagna
    mars_house_moon = whole_sign_house(mars_lon, moon_lon)

    # D9 — navamsha rashi of Mars and Lagna
    mars_d9_rashi = _navamsha_rashi(mars_lon)
    asc_d9_rashi  = _navamsha_rashi(asc_lon)
    mars_house_d9 = (mars_d9_rashi - asc_d9_rashi) % 12 + 1

    mangalik_houses = {1, 2, 4, 7, 8, 12}
    d1_mangalik   = mars_house_d1   in mangalik_houses
    moon_mangalik = mars_house_moon in mangalik_houses
    d9_mangalik   = mars_house_d9   in mangalik_houses

    mangalik_count = sum([d1_mangalik, moon_mangalik, d9_mangalik])

    if mangalik_count == 3:
        severity, is_mangalik = "Strong Mangalik", True
    elif mangalik_count == 2:
        severity, is_mangalik = "Mangalik", True
    elif mangalik_count == 1:
        severity, is_mangalik = "Mild Mangalik", True
    else:
        severity, is_mangalik = "Non-Mangalik", False

    # Classical cancellations
    cancellations = []
    asc_rashi_idx = int(asc_lon / 30.0)
    if asc_rashi_idx in [0, 7]:   # Mesha or Vrishchika lagna
        cancellations.append("Aries/Scorpio Lagna — Mangal in own sign, effect reduced")
    if mars_house_d1 == 10:
        cancellations.append("Mars in 10th house — partial cancellation in many traditions")
    if int(mars_lon / 30.0) in [0, 7]:  # Mars in Mesha or Vrishchika
        cancellations.append("Mars in own rashi — partially cancels dosha")

    return {
        'is_mangalik':       is_mangalik,
        'severity':          severity,
        'mangalik_count':    mangalik_count,
        'd1_mangalik':       d1_mangalik,
        'd1_house':          mars_house_d1,
        'moon_chart_mangalik': moon_mangalik,
        'moon_chart_house':  mars_house_moon,
        'd9_mangalik':       d9_mangalik,
        'd9_house':          mars_house_d9,
        'cancellations':     cancellations,
        'asc_lon':           round(asc_lon, 4),
        'asc_rashi':         RASHI_NAMES[asc_rashi_idx],
        'moon_rashi':        RASHI_NAMES[int(moon_lon / 30.0)],
        'mars_lon':          round(mars_lon, 4),
        'mars_rashi':        RASHI_NAMES[int(mars_lon / 30.0)],
        'planet_positions':  {n: RASHI_NAMES[int(l / 30.0)] for n, l in planet_lons.items()},
    }


# ---------------------------------------------------------------------------
# DIAGNOSTIC
# ---------------------------------------------------------------------------

def debug_nakshatra(birth_date: date, birth_lat: float, birth_lon: float,
                    birth_time_h: int, birth_time_m: int,
                    birth_time_s: int = 0) -> Dict:
    """Print every intermediate value in the janma nakshatra pipeline for
    cross-checking against a reference (Drik Panchang, Astrosage, etc.)."""
    dt = datetime(birth_date.year, birth_date.month, birth_date.day,
                  birth_time_h, birth_time_m, birth_time_s)
    tz = get_timezone(birth_lat, birth_lon)
    utc_dt    = dt.replace(tzinfo=tz).astimezone(ZoneInfo("UTC"))
    tz_offset = get_tz_offset_hours(dt, birth_lat, birth_lon)
    jd        = datetime_to_jd(dt, birth_lat, birth_lon)

    swe.set_sid_mode(swe.SIDM_LAHIRI)
    ayanamsa  = swe.get_ayanamsa(jd)
    moon_trop = swe.calc_ut(jd, swe.MOON)[0][0]
    moon_sid  = (moon_trop - ayanamsa) % 360.0
    nak_name, pada, deg_in_nak = lon_to_nakshatra(moon_sid)

    info = {
        'input_local':      dt.strftime("%Y-%m-%d %H:%M:%S"),
        'timezone':         str(tz),
        'utc_time':         utc_dt.strftime("%Y-%m-%d %H:%M:%S UTC"),
        'tz_offset_hours':  tz_offset,
        'julian_day':       round(jd, 8),
        'ayanamsa_lahiri':  round(ayanamsa, 6),
        'moon_tropical':    round(moon_trop, 6),
        'moon_sidereal':    round(moon_sid, 6),
        'nakshatra':        nak_name,
        'pada':             pada,
        'deg_in_nakshatra': round(deg_in_nak, 4),
    }
    for k, v in info.items():
        print(f"  {k:22s}: {v}")
    return info
