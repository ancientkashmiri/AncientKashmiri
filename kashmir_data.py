# Kashmir Geographic and Cultural Data

INDIA_STATES = {
    "Jammu & Kashmir": {
        "Srinagar": (34.0837, 74.7973),
        "Jammu": (32.7266, 74.8570),
        "Anantnag": (33.7311, 75.1487),
        "Baramulla": (34.2099, 74.3450),
        "Pulwama": (33.8799, 74.8942),
        "Kupwara": (34.5213, 74.2613),
        "Budgam": (33.9374, 74.7184),
        "Ganderbal": (34.2285, 74.7776),
        "Shopian": (33.7163, 74.8368),
        "Kulgam": (33.6443, 75.0177),
        "Bandipora": (34.4190, 74.6394),
        "Kathua": (32.3847, 75.5170),
        "Udhampur": (32.9160, 75.1419),
        "Rajouri": (33.3780, 74.3110),
        "Poonch": (33.7730, 74.0930),
        "Doda": (33.1490, 75.5470),
        "Kishtwar": (33.3130, 75.7660),
        "Ramban": (33.2400, 75.2380),
        "Reasi": (33.0820, 74.8310),
        "Samba": (32.5580, 75.1190),
        "Leh": (34.1526, 77.5771),
        "Kargil": (34.5593, 76.1346),
    },
    "Delhi": {
        "New Delhi": (28.6139, 77.2090),
        "North Delhi": (28.7041, 77.1025),
        "South Delhi": (28.5355, 77.3910),
        "East Delhi": (28.6671, 77.2935),
        "West Delhi": (28.6520, 77.0534),
    },
    "Maharashtra": {
        "Mumbai": (19.0760, 72.8777),
        "Pune": (18.5204, 73.8567),
        "Nagpur": (21.1458, 79.0882),
        "Nashik": (20.0059, 73.7757),
        "Aurangabad": (19.8762, 75.3433),
    },
    "Himachal Pradesh": {
        "Shimla": (31.1048, 77.1734),
        "Dharamsala": (32.2190, 76.3234),
        "Manali": (32.2396, 77.1887),
        "Kullu": (31.9574, 77.1096),
        "Mandi": (31.7080, 76.9320),
    },
    "Punjab": {
        "Amritsar": (31.6340, 74.8723),
        "Ludhiana": (30.9010, 75.8573),
        "Jalandhar": (31.3260, 75.5762),
        "Patiala": (30.3398, 76.3869),
        "Chandigarh": (30.7333, 76.7794),
    },
    "Uttar Pradesh": {
        "Lucknow": (26.8467, 80.9462),
        "Varanasi": (25.3176, 82.9739),
        "Agra": (27.1767, 78.0081),
        "Allahabad": (25.4358, 81.8463),
        "Kanpur": (26.4499, 80.3319),
        "Mathura": (27.4924, 77.6737),
        "Ayodhya": (26.7922, 82.1998),
    },
    "Gujarat": {
        "Ahmedabad": (23.0225, 72.5714),
        "Surat": (21.1702, 72.8311),
        "Vadodara": (22.3072, 73.1812),
        "Rajkot": (22.3039, 70.8022),
    },
    "Rajasthan": {
        "Jaipur": (26.9124, 75.7873),
        "Jodhpur": (26.2389, 73.0243),
        "Udaipur": (24.5854, 73.7125),
        "Bikaner": (28.0229, 73.3119),
    },
    "Karnataka": {
        "Bengaluru": (12.9716, 77.5946),
        "Mysuru": (12.2958, 76.6394),
        "Mangaluru": (12.9141, 74.8560),
        "Hubli": (15.3647, 75.1240),
    },
    "Tamil Nadu": {
        "Chennai": (13.0827, 80.2707),
        "Coimbatore": (11.0168, 76.9558),
        "Madurai": (9.9252, 78.1198),
        "Salem": (11.6643, 78.1460),
    },
    "West Bengal": {
        "Kolkata": (22.5726, 88.3639),
        "Darjeeling": (27.0410, 88.2663),
        "Siliguri": (26.7271, 88.3953),
        "Durgapur": (23.5204, 87.3119),
    },
    "Madhya Pradesh": {
        "Bhopal": (23.2599, 77.4126),
        "Indore": (22.7196, 75.8577),
        "Gwalior": (26.2183, 78.1828),
        "Ujjain": (23.1793, 75.7849),
    },
}

NAKSHATRAS = [
    "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira",
    "Ardra", "Punarvasu", "Pushya", "Ashlesha", "Magha",
    "Purva Phalguni", "Uttara Phalguni", "Hasta", "Chitra", "Swati",
    "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
    "Uttara Ashadha", "Shravana", "Dhanishtha", "Shatabhisha",
    "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
]

RASHIS = [
    "Mesha (Aries)", "Vrishabha (Taurus)", "Mithuna (Gemini)",
    "Karka (Cancer)", "Simha (Leo)", "Kanya (Virgo)",
    "Tula (Libra)", "Vrishchika (Scorpio)", "Dhanu (Sagittarius)",
    "Makara (Capricorn)", "Kumbha (Aquarius)", "Meena (Pisces)"
]

# ---------------------------------------------------------------------------
# KASHMIR VALLEY — District → Town/Mohalla → Villages/Mauzas
# ---------------------------------------------------------------------------

KP_DISTRICTS = [
    "Srinagar", "Baramulla", "Anantnag", "Pulwama", "Budgam",
    "Kupwara", "Ganderbal", "Shopian", "Kulgam", "Bandipora",
]

KP_TOWNS = {
    "Srinagar":  [
        "Habba Kadal", "Rainawari", "Zaina Kadal", "Fateh Kadal",
        "Safa Kadal", "Bohri Kadal", "Aali Kadal", "Nawab Bazar",
        "Shehr-e-Khas", "Khanyar", "Nowhatta", "Maisuma",
        "Barbarshah", "Safakadal", "Karan Nagar", "Gogji Pathri",
        "Bemina", "Hyderpora", "Natipora", "Jawahar Nagar",
        "Indira Nagar", "Rajbagh", "Lal Chowk", "Soura",
        "Nishat", "Harwan", "Shalimar", "Ganderbal Town",
        "Pampore", "Lasjan", "Narbal", "Pantha Chowk",
    ],
    "Baramulla": [
        "Baramulla Town", "Sopore", "Pattan", "Uri",
        "Tangmarg", "Gulmarg", "Rafiabad", "Kreeri",
        "Kunzer", "Boniyar", "Druggmulla", "Kawanpora",
    ],
    "Anantnag":  [
        "Anantnag Town", "Bijbehara", "Islamabad", "Kokernag",
        "Pahalgam", "Dooru", "Shangus", "Vailoo",
        "Srigufwara", "Mattan", "Achabal", "Verinag",
        "Breng Valley", "Qazigund", "Banihal",
    ],
    "Pulwama":   [
        "Pulwama Town", "Pampore", "Tral", "Awantipora",
        "Khrew", "Kakapora", "Rajpora", "Newa",
        "Arihal", "Shadimarg",
    ],
    "Budgam":    [
        "Budgam Town", "Magam", "Beerwah", "Narbal",
        "Chadoora", "Khansahib", "Charar-i-Sharief",
        "Rakh-i-Arth", "Soibugh", "Pakharpora",
    ],
    "Kupwara":   [
        "Kupwara Town", "Handwara", "Karnah", "Lolab",
        "Sogam", "Kralpora", "Drugmulla", "Trehgam",
    ],
    "Ganderbal": [
        "Ganderbal Town", "Kangan", "Lar", "Wakura",
        "Manigam", "Tullamulla", "Shuhama",
    ],
    "Shopian":   [
        "Shopian Town", "Keegam", "Hermain", "Zainpora",
        "Hirpora", "Barbugh", "Chitragam",
    ],
    "Kulgam":    [
        "Kulgam Town", "D.H. Pora", "Devsar", "Frisal",
        "Pahloo", "Yaripora", "Noorabad",
    ],
    "Bandipora": [
        "Bandipora Town", "Hajin", "Sumbal", "Gurez",
        "Ajas", "Tulail", "Sonawari",
    ],
}

KP_VILLAGES = {
    # Srinagar
    "Habba Kadal":    ["Habba Kadal (mohalla)", "Kawdara", "Safakadal", "Maharajgunj"],
    "Rainawari":      ["Rainawari", "Dalgate", "Nallabagh", "Sheikh Mohalla"],
    "Zaina Kadal":    ["Zaina Kadal", "Saraf Kadal", "Kathi Darwaza", "Kralpather"],
    "Fateh Kadal":    ["Fateh Kadal", "Baba Demb", "Maharaj Gunj", "Naidyar"],
    "Safa Kadal":     ["Safa Kadal", "Zukura", "Drujan", "Idgah"],
    "Bohri Kadal":    ["Bohri Kadal", "Chattabal", "Azad Gunj", "Badami Bagh"],
    "Aali Kadal":     ["Aali Kadal", "Sekidafar", "Guru Bazar", "Khankahi Mohalla"],
    "Nawab Bazar":    ["Nawab Bazar", "Kathi Darwaza", "Sopore Gate", "Noorbagh"],
    "Shehr-e-Khas":   ["Shehr-e-Khas", "Lal Chowk Area", "Residency Road", "Polo View"],
    "Khanyar":        ["Khanyar", "Bagh-e-Dilawar Khan", "Syed Ali Akbar Mohalla"],
    "Nowhatta":       ["Nowhatta", "Budshah Chowk", "Noor Bagh", "Gaw Kadal"],
    "Karan Nagar":    ["Karan Nagar", "Gogji Pathri", "Wazir Bagh", "Buchpora"],
    "Gogji Pathri":   ["Gogji Pathri", "Natipora", "Hyderpora", "Bemina"],
    "Soura":          ["Soura", "Baghi Mehtab", "Pantha Chowk", "Nowgam"],
    "Nishat":         ["Nishat", "Cheshmashahi", "Harwan", "Shalimar"],
    "Pampore":        ["Pampore", "Lethpora", "Awantipora", "Pulwama Road"],
    "Narbal":         ["Narbal", "Lasjan", "Rangreth", "Humhama"],
    # Baramulla
    "Baramulla Town": ["Baramulla Town", "Khawajabagh", "Watergam", "Sopore Road"],
    "Sopore":         ["Sopore", "Dangiwacha", "Kralagund", "Arampora"],
    "Pattan":         ["Pattan", "Watlab", "Singhpora", "Nadihal"],
    "Tangmarg":       ["Tangmarg", "Drang", "Kunzer", "Wagoora"],
    "Gulmarg":        ["Gulmarg", "Affarwat", "Khilanmarg", "Kongdoori"],
    "Uri":            ["Uri", "Boniyar", "Salamabad", "Churanda"],
    # Anantnag
    "Anantnag Town":  ["Anantnag Town", "Khanbal", "Shahabad", "Lal Chowk Anantnag"],
    "Bijbehara":      ["Bijbehara", "Wanpoh", "Achabal", "Arwani"],
    "Kokernag":       ["Kokernag", "Daksum", "Verinag", "Pahalgam Road"],
    "Pahalgam":       ["Pahalgam", "Aru", "Betaab Valley", "Chandanwari"],
    "Mattan":         ["Mattan", "Martand", "Tral Road", "Sagam"],
    "Achabal":        ["Achabal", "Bijbehara Road", "Watchiloo", "Semthan"],
    # Pulwama
    "Pulwama Town":   ["Pulwama Town", "Tral", "Rajpora", "Shadimarg"],
    "Awantipora":     ["Awantipora", "Pampore", "Kakapora", "Lassipora"],
    "Khrew":          ["Khrew", "Drabgam", "Newa", "Arihal"],
    "Kakapora":       ["Kakapora", "Mir Mohalla", "Namblabal", "Samboora"],
    # Budgam
    "Budgam Town":    ["Budgam Town", "Chadoora", "Nagam", "Ichgam"],
    "Magam":          ["Magam", "Warpora", "Charar-i-Sharief Road", "Rakh"],
    "Beerwah":        ["Beerwah", "Sultanpora", "Khag", "Wathoora"],
    "Charar-i-Sharief": ["Charar-i-Sharief", "Dobiwan", "Durganag", "Yousmarg"],
    # Kupwara
    "Kupwara Town":   ["Kupwara Town", "Drugmulla", "Vilgam", "Kralpora"],
    "Handwara":       ["Handwara", "Langate", "Khumriyal", "Sogam"],
    "Karnah":         ["Karnah", "Teetwal", "Shardi", "Keran"],
    # Ganderbal
    "Ganderbal Town": ["Ganderbal Town", "Wakura", "Tullamulla (Tulmul)", "Shuhama"],
    "Kangan":         ["Kangan", "Gund", "Sonamarg", "Lar"],
    "Tullamulla":     ["Tullamulla (Tulmul)", "Wakura", "Manigam", "Shuhama"],
    # Shopian
    "Shopian Town":   ["Shopian Town", "Zainpora", "Keegam", "Hermain"],
    "Keegam":         ["Keegam", "Pinjoora", "Chitragam", "Barbugh"],
    # Kulgam
    "Kulgam Town":    ["Kulgam Town", "Devsar", "D.H. Pora", "Noorabad"],
    "D.H. Pora":      ["D.H. Pora", "Yaripora", "Frisal", "Pahloo"],
    # Bandipora
    "Bandipora Town": ["Bandipora Town", "Hajin", "Sumbal", "Sonawari"],
    "Hajin":          ["Hajin", "Ajas", "Palhalan", "Kaloosa"],
    "Sumbal":         ["Sumbal", "Asham", "Sopore Road", "Pattan Road"],
}

# Comprehensive list of Kashmiri Pandit surnames
KP_SURNAMES = [
    "— Optional —",
    # Most common / widespread
    "Kaul", "Koul", "Bhat", "Bhatt", "Pandit", "Raina", "Mattoo",
    "Wakhloo", "Dhar", "Tickoo", "Tiku", "Kachru", "Sapru", "Razdan",
    "Nehru", "Bazaz", "Zutshi", "Jotishi", "Ganjoo", "Jalali",
    "Handoo", "Handu", "Munshi", "Munsi", "Sopori", "Wangnoo",
    "Gadoo", "Gadu", "Haksar", "Kaur", "Kaw", "Kak",
    "Sharga", "Shargha", "Watal", "Wattal", "Ogra", "Ogra",
    "Butt", "Butt (KP)", "Kilam", "Kilaam", "Nath", "Nath",
    # By region / origin
    "Srinagri", "Kashmiri", "Pandita",
    # Shakha / Priestly
    "Jyotishi", "Purohit", "Acharya", "Shastri", "Upadhyay",
    # Occupational / title surnames
    "Divan", "Diwan", "Vakil", "Munshi", "Hakim", "Vaid",
    "Wazir", "Waza", "Dar", "Khar", "Malhotra",
    # Less common but authentic KP surnames
    "Akhoon", "Ambardar", "Amla", "Angroo", "Anjoo",
    "Ardoo", "Arjoo", "Aziz", "Badam", "Bakshi",
    "Bamzai", "Bandhu", "Bangroo", "Baroo", "Beri",
    "Bhan", "Bhawan", "Boga", "Brar", "Broo",
    "Chandroo", "Chattoo", "Chawla", "Chroo", "Chutoo",
    "Daga", "Dagoo", "Damas", "Damu", "Dand",
    "Dandoo", "Dassi", "Dass", "Deewana", "Desai",
    "Deva", "Dhami", "Dhir", "Dhobi", "Didda",
    "Dogra", "Doomchi", "Doon", "Doondi", "Drab",
    "Dulloo", "Fotedar", "Gadda", "Gasha", "Gawkadal",
    "Ghai", "Ghosh", "Gigoo", "Goga", "Gogoo",
    "Googoo", "Goria", "Goroo", "Gossain", "Gour",
    "Groo", "Gudoo", "Gulati", "Gupta", "Guru",
    "Gurutu", "Habba", "Hajan", "Halwai", "Hanjoo",
    "Haq", "Haqdad", "Hatoo", "Hatti", "Hazari",
    "Heroo", "Hingoo", "Hingraj", "Hooda", "Hoora",
    "Horo", "Ibrahimpur", "Ithoo", "Jagoo", "Jakoo",
    "Jalla", "Jandoo", "Jangoo", "Jani", "Janoo",
    "Jantoo", "Jarnail", "Jatoo", "Jawla", "Jelani",
    "Jha", "Jhoo", "Jotoo", "Joyal", "Kachoo",
    "Kadal", "Kadoo", "Kak", "Kakoo", "Kala",
    "Kalbag", "Kam", "Kamoo", "Kanchan", "Kanoo",
    "Kantha", "Kapila", "Kapo", "Kapoo", "Kara",
    "Karoo", "Kashmiri", "Kata", "Katoo", "Kaur",
    "Kaushal", "Kawa", "Keer", "Khajoor", "Khan",
    "Khar", "Khazir", "Khosa", "Kichloo", "Kiloo",
    "Kohli", "Kol", "Koli", "Koo", "Koosa",
    "Kota", "Kotru", "Kotwal", "Koul", "Kounsar",
    "Kram", "Kroo", "Kuchhoo", "Kuchloo", "Kudoo",
    "Kulbhushan", "Kumari", "Kundi", "Lahoo", "Lala",
    "Lalwani", "Lama", "Lamba", "Langar", "Lassa",
    "Lassoo", "Latto", "Laven", "Lavoo", "Lazar",
    "Lone", "Loo", "Looh", "Lool", "Lota",
    "Lota (KP)", "Mahajan", "Mala", "Malhotra", "Malla",
    "Mallah", "Malloo", "Manchanda", "Manda", "Manoo",
    "Mantoo", "Maroo", "Mattan", "Matto", "Mehjoor",
    "Mehra", "Mir", "Miroo", "Mistry", "Mogha",
    "Monga", "Monoo", "Mujoo", "Mungloo", "Muroo",
    "Mushroo", "Nadir", "Nagoo", "Naji", "Namboo",
    "Namgyal", "Nanda", "Nandoo", "Nanji", "Naq",
    "Nasir", "Nasta", "Nath", "Nayoo", "Nenoo",
    "Niboo", "Niloo", "Nilufar", "Noorbakhsh", "Norkoo",
    "Pampori", "Pandita", "Panjabi", "Pannu", "Pargal",
    "Parra", "Parrikar", "Partoo", "Parvez", "Pasha",
    "Patel", "Patwari", "Payne", "Peer", "Pehloo",
    "Peshin", "Petha", "Piloo", "Pir", "Pita",
    "Pitamber", "Piyar", "Pocha", "Popoo", "Poshwal",
    "Poshwala", "Posta", "Pranoo", "Qadri", "Qazi",
    "Raaj", "Rabb", "Rafoo", "Raga", "Raghunath",
    "Rahen", "Rahi", "Rai", "Raizada", "Rajdan",
    "Rake", "Rama", "Ramoo", "Rana", "Rangroo",
    "Ranjoo", "Rathore", "Rattan", "Rauf", "Razoo",
    "Rehman", "Renoo", "Reshoo", "Reshi", "Rhashan",
    "Rishi", "Rohoo", "Rosoo", "Rouf", "Rungta",
    "Rustam", "Sadhu", "Sahib", "Sahoo", "Saif",
    "Saifu", "Saigal", "Saini", "Sajjan", "Sakhoo",
    "Samoo", "Sanjoo", "Sapoo", "Saran", "Saroo",
    "Sartaj", "Sathu", "Sawhney", "Sayeed", "Saygal",
    "Sethi", "Shah", "Shahoo", "Shanoo", "Shastri",
    "Sheroo", "Shetty", "Shivoo", "Shora", "Shori",
    "Shukla", "Shyam", "Sikka", "Simboo", "Simoo",
    "Singh", "Singhvi", "Sinha", "Sirtaj", "Sondhi",
    "Soni", "Sool", "Sooni", "Soora", "Srivastva",
    "Sukha", "Sukhoo", "Sultan", "Suri", "Swami",
    "Tagar", "Takia", "Talloo", "Tamber", "Tandel",
    "Tandon", "Taneo", "Tanga", "Tanoo", "Taploo",
    "Tapoo", "Taroo", "Tayal", "Tenoo", "Tiku",
    "Tilan", "Tota", "Triloknath", "Troo", "Tulloo",
    "Udar", "Udoo", "Ulla", "Uppal", "Urfi",
    "Usman", "Vakil", "Vasudeva", "Verma", "Vijay",
    "Vimal", "Viroo", "Vishal", "Vohra", "Wafoo",
    "Wakhoo", "Wal", "Wali", "Wallo", "Wanchu",
    "Wani", "Wanoo", "Wanpoo", "Wardoo", "Waroo",
    "Wazoo", "Wazir", "Yadav", "Yatoo", "Yoo",
    "Yoosuf", "Yusuf", "Zafar", "Zahoor", "Zainoo",
    "Zaka", "Zaroo", "Zargar", "Zatoo", "Zindoo",
    "Zitoo", "Zoo", "Zore", "Zutoo",
]

# ---------------------------------------------------------------------------
# ASHTA BHAIRAVAS OF KASHMIR (Eight directional guardians per Nilamata Purana
# and Trika tradition — each guards a mohalla / zone of the valley)
# ---------------------------------------------------------------------------

ASHTA_BHAIRAVAS = [
    {
        "name": "Vetalraja Bhairava",
        "region": "Rainawari, Dal Lake area",
        "direction": "North",
        "notes": "Guardian of Rainawari and the Dal Lake shore",
    },
    {
        "name": "Anandeshwara Bhairava",
        "region": "Sathu Barbar Shah, Amira Kadal, Ganpatyar, Maisuma",
        "direction": "North-East",
        "notes": "Guardian of central Srinagar mohallas",
    },
    {
        "name": "Tushkaraja (Turushkaraja) Bhairava",
        "region": "Habba Kadal, Doodh Ganga confluence, Habbak-kadal",
        "direction": "East",
        "notes": "Guardian of the Habba Kadal bridge and Doodh Ganga confluence",
    },
    {
        "name": "Bahukhatkeshwara Bhairava",
        "region": "Safa Kadal, Chhattabal",
        "direction": "South-East",
        "notes": "Guardian of Safa Kadal and Chhattabal area",
    },
    {
        "name": "Purnaraja (Pooranraja) Bhairava",
        "region": "Hari Parbat, Ali Kadal, Safa Kadal vicinity",
        "direction": "South",
        "notes": "Guardian of Hari Parbat and surrounding areas",
    },
    {
        "name": "Mangalaraja (Mangaleshwara) Bhairava",
        "region": "Fateh Kadal, Zaina Kadal, Bohri Kadal",
        "direction": "South-West",
        "notes": "Guardian of the old city kadal (bridge) belt",
    },
    {
        "name": "Jayaksena Bhairava",
        "region": "Zaina Kadal (left bank)",
        "direction": "West",
        "notes": "Guardian of the left bank of Zaina Kadal area",
    },
    {
        "name": "Vishvaksena Bhairava",
        "region": "Beyond Zaina Kadal, outer Srinagar",
        "direction": "North-West",
        "notes": "Guardian of areas beyond Zaina Kadal towards the valley",
    },
]

# ---------------------------------------------------------------------------
# OTHER LOCAL / AREA-SPECIFIC BHAIRAVAS
# ---------------------------------------------------------------------------

LOCAL_BHAIRAVAS = [
    {
        "name": "Nandikeshwara Bhairava",
        "region": "Sumbal, Bandipora",
        "notes": "Also known as Nandkishor / Nandkeshwar Bhairava; temple at Sumbal",
    },
    {
        "name": "Bhimareja Bhairava",
        "region": "Prayagraj Shadipura, Srinagar",
        "notes": "Associated with Shadipura area",
    },
    {
        "name": "Bhuteshwara Bhairava",
        "region": "Tulmul (Tullamulla), Ganderbal",
        "notes": "Guardian of the Tulmul (Kheer Bhawani) area",
    },
    {
        "name": "Kalabhairava",
        "region": "Universal / all Kashmir",
        "notes": "Chief of the 64 Bhairavas; widely worshipped across the valley",
    },
    {
        "name": "Batuka Bhairava",
        "region": "Universal / Herath ritual",
        "notes": "Child form of Bhairava; central to Herath (Kashmiri Shivratri) Vatuk Puja",
    },
    {
        "name": "Swarna Akarshana Bhairava",
        "region": "Srinagar / wider valley",
        "notes": "Wealth-conferring form; worshipped in Srinagar households",
    },
    {
        "name": "Samhara Bhairava",
        "region": "Wider valley",
        "notes": "Dissolution aspect; part of the 8-Bhairava cycle in Kashmir Shaivism",
    },
    {
        "name": "Unmatta Bhairava",
        "region": "Wider valley",
        "notes": "The ecstatic form; associated with tantric Trika lineages",
    },
]

# ---------------------------------------------------------------------------
# KUL DEVI BY DISTRICT (regional mapping — tentative)
# ---------------------------------------------------------------------------

KUL_DEVI_BY_DISTRICT = {
    "Srinagar": {
        "primary": "Sharika Devi (Chakreshwari)",
        "temple": "Hari Parbat, Srinagar",
        "notes": "Principal Kul Devi of old-city Srinagar KP families. The hill itself is "
                 "held to be the goddess who crushed the demon Jalodbhava.",
        "also": ["Ragnya Devi / Kheer Bhawani"],
    },
    "Ganderbal": {
        "primary": "Ragnya Devi (Kheer Bhawani)",
        "temple": "Tullamulla (Tulmul), Ganderbal",
        "notes": "Most widely venerated Kul Devi across all KP families; "
                 "Zyeth Ashtami annual mela draws thousands.",
        "also": ["Sharika Devi"],
    },
    "Anantnag": {
        "primary": "Bhadrakali",
        "temple": "Anantnag district temples",
        "notes": "South Kashmir families traditionally associate with Bhadrakali; "
                 "also Martand Surya as Kul Devta.",
        "also": ["Tripura Sundari", "Jwala Devi"],
    },
    "Pulwama": {
        "primary": "Jwala Devi",
        "temple": "Khrew, Pulwama",
        "notes": "Families from Khrew and surrounding Pulwama villages venerate Jwala Devi.",
        "also": ["Bhadrakali"],
    },
    "Baramulla": {
        "primary": "Sharika Devi / Ragnya Devi",
        "temple": "Hari Parbat (Srinagar) / Tulmul (Ganderbal)",
        "notes": "North Kashmir KP families generally share Srinagar-belt Kul Devis.",
        "also": ["Sharada Devi (Sharada Peeth, Sharda, PoK)"],
    },
    "Budgam": {
        "primary": "Sharika Devi",
        "temple": "Hari Parbat, Srinagar",
        "notes": "Central Kashmir (Budgam) families largely follow Srinagar Kul Devi tradition.",
        "also": ["Ragnya Devi"],
    },
    "Kupwara": {
        "primary": "Sharada Devi",
        "temple": "Sharada Peeth, Sharda (now PoK)",
        "notes": "Far north families traditionally venerated Sharada; now worship at proxy shrines.",
        "also": ["Ragnya Devi"],
    },
    "Shopian": {
        "primary": "Bhadrakali",
        "temple": "South Kashmir temples",
        "notes": "South-west Kashmir families (Shopian belt) primarily venerate Bhadrakali.",
        "also": ["Jwala Devi"],
    },
    "Kulgam": {
        "primary": "Bhadrakali / Tripura Sundari",
        "temple": "South Kashmir temples",
        "notes": "Deep south Kashmir families venerate Bhadrakali and Tripura Sundari.",
        "also": ["Ragnya Devi"],
    },
    "Bandipora": {
        "primary": "Ragnya Devi (Kheer Bhawani)",
        "temple": "Tulmul, Ganderbal (also Nandkishwar, Sumbal)",
        "notes": "North-east Kashmir families; Nandkeshwar Bhairava is local Kshetrapala.",
        "also": ["Sharika Devi"],
    },
}

# ---------------------------------------------------------------------------
# KUL DEVTA BY DISTRICT (male deity — tentative)
# ---------------------------------------------------------------------------

KUL_DEVTA_BY_DISTRICT = {
    "Srinagar":  {
        "primary": "Shiva (Shankaracharya / Jyeshtheshwara)",
        "temple":  "Shankaracharya Hill, Srinagar",
        "notes":   "The Shankaracharya Shiva temple (Jyeshtheshwara) atop the hill has "
                   "been the presiding Kul Devta for most old-city Srinagar families.",
    },
    "Ganderbal": {
        "primary": "Shiva (Amarnath / Bhuteshwara)",
        "temple":  "Amarnath, Pahalgam; Bhuteshwara temple Tulmul area",
        "notes":   "Universal Shiva worship; Bhuteshwara Bhairava local guardian.",
    },
    "Anantnag":  {
        "primary": "Surya (Martand)",
        "temple":  "Martand Sun Temple, Mattan, Anantnag",
        "notes":   "Ancient Surya temple (8th c. CE, Lalitaditya) — primary Kul Devta "
                   "for Anantnag-belt families.",
    },
    "Pulwama":   {
        "primary": "Shiva / Surya",
        "temple":  "Awantipur Shiva temple, Avantishwara",
        "notes":   "Awantishwara and Awantiswamin temples (Avantipora) — major Shiva and "
                   "Vishnu shrines for Pulwama-belt families.",
    },
    "Baramulla":  {
        "primary": "Shiva (Bhimashankar)",
        "temple":  "Baramulla area Shiva shrines",
        "notes":   "North Kashmir families predominantly Shaiva.",
    },
    "Budgam":    {
        "primary": "Shiva",
        "temple":  "Charar-i-Sharief (originally Shaiva site)",
        "notes":   "Central Kashmir families — primarily Shaiva Kul Devta.",
    },
    "Kupwara":   {
        "primary": "Shiva / Vishnu",
        "temple":  "Local shrines; Sharada Peeth (PoK)",
        "notes":   "Far north — Shaiva and Vaishnava traditions both present.",
    },
    "Shopian":   {
        "primary": "Shiva",
        "temple":  "South Kashmir Shiva shrines",
        "notes":   "South-west belt — primarily Shaiva tradition.",
    },
    "Kulgam":    {
        "primary": "Shiva / Vishnu",
        "temple":  "South Kashmir temples",
        "notes":   "Deep south — both Shaiva and Vaishnava lineages present.",
    },
    "Bandipora": {
        "primary": "Shiva (Nandikeshwara)",
        "temple":  "Nandkishwar temple, Sumbal",
        "notes":   "Nandikeshwara (Nandi form of Shiva) is presiding Kul Devta for "
                   "Bandipora / Sumbal families.",
    },
}

# ---------------------------------------------------------------------------
# GOTRAS with associated KP surnames (from traditional records)
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# SURNAME → GOTRA(S) MAP
# Source: Traditional KP gotra table (image provided by user).
# Each surname maps to its possible gotra(s) only — no other surnames listed.
# Tentative: verify with a Pandit of the region.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# SURNAME → GOTRA(S) MAP
# Source: Traditional KP gotra-surname table (image provided).
# Maps each KP surname to its possible gotra(s) only.
# Tentative: verify with a Pandit of the region.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# SURNAME (Nick Name) → GOTRA(S) MAP
# Source: Bhannamasis & Malmasis gotra tables (PDF provided).
# Each entry: Nick Name → list of full compound gotra lineage names exactly
# as they appear in the document. Multiple entries = multiple gotras possible.
# Tentative: verify with a Pandit of the region.
# ---------------------------------------------------------------------------

SURNAME_GOTRA_MAP = {
    "Aima":         ["Datthtreya (Koul)"],
    "Amhardar":     ["Pat Svamina Kaushika"],
    "Babu":         ["Datthtreya (Koul)"],
    "Badgami":      ["Deva Kucha Atreya"],
    "Bakaya":       ["Paladeva Vasgargya"],
    "Bakhshi":      ["Dar Varshaganya", "Svamina Shandalya"],
    "Bali":         ["Svamina Bhargava"],
    "Bamtsunt":     ["Datthtreya (Koul)"],
    "Bamzai":       ["Datthtreya (Koul)"],
    "Bandar":       ["Kantha Dhaumyana Laugakshi Gautama"],
    "Bangi":        ["Dar Bharadwaja"],
    "Bangru":       ["Paladeva Vasgargya"],
    "Barbuz":       ["Varshayani"],
    "Bataphalu":    ["Deva Shandalya"],
    "Battiv":       ["Svamina Bhargava"],
    "Bazari":       ["Svamina Bharadvaja"],
    "Bazaz":        ["Svamina Gautama"],
    "Bhan":         ["Deva Gargya", "Raj Bhut Logaskhi Deval"],
    "Bhandari":     ["Vasishta Svamina Maudgalya"],
    "Bhatt":        ["Dar Kapisthala", "Dat Dat Shalan Kautsa",
                     "Deva Bharadwaja", "Deva Gautama", "Deva Kaushika",
                     "Kautsa Atreya", "Kaushika Bhardwaja",
                     "Kash Aupamanyava", "Mitra Shandalya",
                     "Nanda Koshk", "Raj Dat Atreya Shalan Kautsa",
                     "Sharman Bharadwaja", "Shandalya Bharadwaja",
                     "Sharman Kautsa", "Svamina Koshk Bharadwaja",
                     "Svamina Shandalya", "Svamina Vasishta Bharadwaja",
                     "Svamina Vatsya Aupamanyava", "Wasishta"],
    "Bhuni":        ["Svamina Maudgalya"],
    "Bindri":       ["Wasadeva Palagargya"],
    "Bira":         ["Pat Svamina Kaushika"],
    "Bradi":        ["Deva Kashyap Maudgalya Kashyap", "Dev Svamina Maudgalya"],
    "Braru":        ["Pat Svamina Kaushika"],
    "Breth":        ["Kantha Dhaumyana Laugakshi Gautama"],
    "Buju":         ["Datthtreya (Koul)"],
    "Buni":         ["Svamina Maudgalya"],
    "Chacha":       ["Pat Svamina Kaushika", "Ratra Bhargava"],
    "Chaghat":      ["Pat Svamina Kaushika"],
    "Chaka":        ["Svamina Atreya"],
    "Chakan":       ["Svamina Gotam Gosh Vas Aupamanyava"],
    "Chana":        ["Svamina Maudgalya"],
    "Chandra":      ["Bhava Kapishthala"],
    "Chandru":      ["Karchanda Shandale"],
    "Charangu":     ["Svamina Gautama"],
    "Chillum":      ["Svamina Gautama"],
    "Choku":        ["Svamina Gotam Laugakshi"],
    "Chothai":      ["Svamina Warshaganya"],
    "Choudhri":     ["Artha Varshaganya Shandalya Bharadwaj"],
    "Chowdhri":     ["Datthtreya (Koul)"],
    "Chhotu":       ["Svamina Gotam Laugakshi"],
    "Dandar":       ["Datthtreya (Koul)"],
    "Dangar":       ["Datthtreya (Koul)"],
    "Dar":          ["Dar Bharadwaja"],
    "Dassu":        ["Kanth Kasahap"],
    "Deva":         ["Deva Bharadwaja Kaushika"],
    "Dewani":       ["Svamina Maudgalya"],
    "Divali":       ["Svamina Bharadwaja Dhuni Kashypa Gautama Laugakshi"],
    "Dout":         ["Datthtreya (Koul)"],
    "Drabi":        ["Datthtreya (Koul)"],
    "Duda":         ["Svamina Warshaganya"],
    "Durani":       ["Pat Svamina Kaushika"],
    "Duru":         ["Raj Shandalya"],
    "Fata":         ["Svamina Gautama Laugakshi"],
    "Fotedar":      ["Pat Svamina Kaushika"],
    "Gaddu":        ["Sharman Atreya"],
    "Gadwali":      ["Svamina Atreya"],
    "Gadar":        ["Deva Bharadwaja"],
    "Gagar":        ["Svamina Gautama"],
    "Galikrapa":    ["Svamina Maudgalya"],
    "Ganju":        ["Pat Svamina Kaushika"],
    "Garyali":      ["Svamina Bharadvaja"],
    "Ghasi":        ["Svamina Vas Atreya"],
    "Gigu":         ["Svamina Aupamanyava"],
    "Giru":         ["Bhuta Aupamanyava Shalan Kayana"],
    "Gurut":        ["Svamina Gautama"],
    "Hak":          ["Datthtreya (Koul)"],
    "Hakachar":     ["Raj Kaushika"],
    "Hakim":        ["Deva Gautama Laugakshi"],
    "Hangal":       ["Svamina Warshaganya"],
    "Handu":        ["Mitra Kashyapa", "Svamina Atreya",
                     "Svamina Vasishta Bharadwaja"],
    "Hapa":         ["Atri Bhargaya"],
    "Hastiwal":     ["Kantha Dhaumyana Laugakshi Gautama"],
    "Hukku":        ["Dev Wasishta", "Svamina Vasishta Bharadwaja"],
    "Jala":         ["Pat Svamina Kaushika"],
    "Jalali":       ["Datthtreya (Koul)"],
    "Jan":          ["Svamina Bharadvaja"],
    "Jatu":         ["Deva Bharadwaja"],
    "Jawansher":    ["Dar Bharadwaja"],
    "Jinsi":        ["Datthtreya (Koul)"],
    "Jogi":         ["Dar Shandalya"],
    "Jota":         ["Datthtreya (Koul)"],
    "Kachru":       ["Dar Varshaganya", "Pat Svamina Kaushika"],
    "Kadalabuju":   ["Paladeva Vasgargya"],
    "Kak":          ["Datthtreya (Koul)", "Deva Parashara", "Svamina Gautama"],
    "Kala":         ["Svamina Atreya"],
    "Kakapuri":     ["Svamina Gautama"],
    "Kalla":        ["Bhava Kapishthala"],
    "Kallu":        ["Deva Bharadwaja"],
    "Kalu":         ["Pat Svamina Kaushika", "Dev Aupamanyava",
                     "Svamina Bharadwaja Vas Atre"],
    "Kandar":       ["Svamina Maudgalya"],
    "Kanth":        ["Svamina Maudgalya"],
    "Kar":          ["Deva Kantha Kashyapa", "Karchanda Shandale"],
    "Karawani":     ["Deva Shandalya"],
    "Karihalu":     ["Svamina Gotam Bharadwaja"],
    "Karnel":       ["Varshayani"],
    "Kasab":        ["Dat Dat Shalan Kautsa"],
    "Kasid":        ["Svamina Warshaganya"],
    "Kashgari":     ["Rishi Kaushika"],
    "Kathju":       ["Svamina Warshaganya"],
    "Kav":          ["Kantha Dhaumyana Laugakshi Gautama", "Paldeva Vasagargya"],
    "Kemdal":       ["Svamina Gotam Bharadwaja"],
    "Kem":          ["Dev Vishamitra Varshaganya"],
    "Keni":         ["Datthtreya (Koul)", "Svamina Gautama"],
    "Khaibri":      ["Bhava Kapishthala"],
    "Khanakatu":    ["Svamina Hasya Dvaseya"],
    "Khar":         ["Svamina Bharadvaja", "Svamina Bharadwaja"],
    "Khari":        ["Dat Was"],
    "Khashu":       ["Dev Aupamanyava", "Paladeva Vasgargya"],
    "Khaumush":     ["Dat Dat Shalan Kautsa"],
    "Khod":         ["Raj Kaushika"],
    "Khosa":        ["Svamina Gautama"],
    "Khoshu":       ["Paldeva Vasagargya"],
    "Khurdi":       ["Deva Bharadwaja", "Pat Svamina Kaushika"],
    "Kichlu":       ["Paladeva Vasgargya"],
    "Kissu":        ["Datthtreya (Koul)"],
    "Kokru":        ["Paladeva Vasgargya"],
    "Kotar":        ["Ratra Varshaganya"],
    "Kothdar":      ["Datthtreya (Koul)"],
    "Koul":         ["Svamina Rishi Kanya Gargya",
                     "Shalan Kautsa Sharman Gusha Watsya Aupamanyava",
                     "Datthtreya (Koul)"],
    "Kukru":        ["Paldeva Vasagargya", "Svamina Koshk Bharadwaja"],
    "Kutsru":       ["Svamina Bharadwaja"],
    "Kyani":        ["Pat Svamina Kaushika"],
    "Labru":        ["Svamina Kantha Kashyapa", "Svamina Maudgalya",
                     "Svamina Gotam Shandalya"],
    "Ladakhi":      ["Datthtreya (Koul)"],
    "Lala":         ["Svamina Maudgalya"],
    "Lange":        ["Svamina Warshaganya"],
    "Langer":       ["Svamina Gautama", "Svamina Vasa Gargya"],
    "Lattu":        ["Bhava Kapishthala"],
    "Lidi":         ["Dar Kapisthala"],
    "Machama":      ["Svamina Gargya"],
    "Madan":        ["Svamina Maudgalya"],
    "Mala":         ["Paladeva Vasgargya"],
    "Malik":        ["Dat Dat Shalan Kautsa"],
    "Malla":        ["Paldeva Vasagargya"],
    "Mam":          ["Pat Svamina Kaushika", "Paladeva Vasgargya"],
    "Mandal":       ["Datthtreya (Koul)"],
    "Mantu":        ["Kara Shandalya"],
    "Manwotu":      ["Svamina Gautama"],
    "Mattu":        ["Pat Svamina Kaushika", "Ratra Vishwamitra Agastya"],
    "Mazari":       ["Svamina Maudgalya"],
    "Mekhzin":      ["Datthtreya (Koul)"],
    "Meva":         ["Dev Aupamanyava"],
    "Mich":         ["Dar Kapisthala Upamanuva"],
    "Mirakhur":     ["Paladeva Vasgargya"],
    "Miskin":       ["Svamina Bharadvaja"],
    "Misri":        ["Dar Bharadwaja", "Pat Svamina Kaushika",
                     "Paladeva Vasgargya"],
    "Miyan":        ["Svamina Bharadvaja"],
    "Mogal":        ["Sharman Kautsa"],
    "Mota":         ["Dar Dev Shalan Kapi"],
    "Moza":         ["Datthtreya (Koul)"],
    "Muj":          ["Svamina Maudgalya"],
    "Muhtasib":     ["Datthtreya (Koul)", "Kantha Dhaumyana Laugakshi Gautama"],
    "Muki":         ["Wardhatta Shalana Kucha"],
    "Mukka":        ["Shalan Kautsa Sharman Gusha Watsya Aupamanyava"],
    "Munga":        ["Paladeva Vasgargya"],
    "Munshi":       ["Svamina Bharadvaja"],
    "Mushran":      ["Svamina Maudgalya"],
    "Muttu":        ["Dar Dev Shalana Kaushika"],
    "Nagari":       ["Datthtreya (Koul)", "Kaushika Bhardwaja"],
    "Nakhasi":      ["Ishwar Shandalya Kusha"],
    "Naqib":        ["Svamina Gautama"],
    "Nari":         ["Svamina Shandalya"],
    "Padar":        ["Datthtreya (Koul)"],
    "Padi":         ["Svamina Gan Kaushika"],
    "Padora":       ["Svamina Gautama"],
    "Pahalwan":     ["Datthtreya (Koul)"],
    "Pandit":       ["Pat Svamina Kaushika", "Pat Svamina Deva Ratra Parwara",
                     "Deva Laugakshi", "Dev Aupamanyava",
                     "Nanda Kaushika Bharadwaja", "Vatsya Gusha Aupamanyava"],
    "Panzu":        ["Pat Svamina Kaushika"],
    "Parimu":       ["Svamina Gautama"],
    "Parikala":     ["Dar Bharadwaja"],
    "Partazi":      ["Raj Dhattatreya"],
    "Pat":          ["Paldeva Vasagargya"],
    "Patar":        ["Bhava Kapishthala Kaushika"],
    "Peshen":       ["Bhuta Was Aupamanyava Laugakshi"],
    "Peshin":       ["Bhuta Vatsya Aupamanyava"],
    "Piala":        ["Svamina Gautama"],
    "Pir":          ["Paldeva Vasagargya", "Paladeva Vasgargya"],
    "Pishen":       ["Bhuta Aupamanyava Vatsya Laugakshi"],
    "Put":          ["Svamina Maudgalya", "Paladeva Vasgargya"],
    "Purbi":        ["Deva Gautama"],
    "Qandahari":    ["Dar Bharadwaja"],
    "Qazi":         ["Svamina Gautama"],
    "Raina":        ["Dat Sharman Kantha Kashyapa",
                     "Svamina Gautama Atreya Shalan Kucha"],
    "Rangateng":    ["Wasishta"],
    "Ratiz":        ["Datthtreya (Koul)"],
    "Raval":        ["Ishwar Shandalya Kusha"],
    "Razdan":       ["Kantha Dhaumyana Laugakshi Gautama",
                     "Dhaumyayana", "Kanth Kasahap",
                     "Svamina Gautama", "Svamina Gotam Shandalya",
                     "Svamina Gotam Shalan Kucha Atreya",
                     "Svamina Maudgalya"],
    "Sabani":       ["Deva Bharadwaja"],
    "Safaya":       ["Dar Varshaganya", "Dar Wasak Shandilya",
                     "Deva Varshaganya Shandilya"],
    "Sahib":        ["Datthtreya (Koul)"],
    "Said":         ["Mitra Svamina Kaushika Atreya"],
    "Salman":       ["Pat Svamina Kaushika", "Datthtreya (Koul)"],
    "Sapru":        ["Dipat Saman Aupamanyava"],
    "Sav":          ["Sharman Kautsa"],
    "Sazawul":      ["Dat Varshaganya"],
    "Shah":         ["Kantha Dhaumyana Laugakshi Gautama"],
    "Shair":        ["Kantha Dhaumyana Laugakshi Gautama"],
    "Shal":         ["Svamina Atreya"],
    "Shali":        ["Dar Varshaganya"],
    "Shanglu":      ["Pat Svamina Kaushika"],
    "Shargha":      ["Datthtreya (Koul)"],
    "Shoga":        ["Datthtreya (Koul)"],
    "Shopuri":      ["Dev Wasishta"],
    "Shora":        ["Svamina Maudgalya"],
    "Shunglu":      ["Raj Vasisht"],
    "Sibbu":        ["Bhava Kapishthala"],
    "Sikh":         ["Svamina Atreya"],
    "Singhari":     ["Datthtreya (Koul)"],
    "Sopuri-Pandit":["Paladeva Vasgargya"],
    "Sultan":       ["Datthtreya (Koul)"],
    "Sulu":         ["Pat Svamina Kaushika"],
    "Sum":          ["Svamina Vasa Gargya"],
    "Taku":         ["Svamina Maudgalya"],
    "Tangan":       ["Kanth Kasahap"],
    "Tarivala":     ["Svamina Gautama"],
    "Tava":         ["Svamina Gautama"],
    "Teng":         ["Pat Svamina Kaushika"],
    "Thakur":       ["Bhuta Was Aupamanyava Laugakshi", "Svamina Kaushika"],
    "Thapal":       ["Svamina Gautama"],
    "Thalatsur":    ["Dar Bharadwaja", "Svamina Gautama"],
    "Thela":        ["Sharman Kautsa"],
    "Thogan":       ["Deva Parashara"],
    "Thusu":        ["Svamina Was Atreya", "Svamina Vas Atreya"],
    "Tikku":        ["Svamina Bharadvaja"],
    "Tilwan":       ["Shalan Kautsa Sharman Gusha Watsya Aupamanyava"],
    "Tota":         ["Datthtreya (Koul)"],
    "Trakari":      ["Ratra Vishwamitra Vasishta"],
    "Tritshal":     ["Pat Svamina Kaushika"],
    "Tritsha":      ["Dar Bharadwaja"],
    "Tsrungu":      ["Deva Vardhatta Shalan Kaushika"],
    "Tsul":         ["Svamina Gotam Atreya"],
    "Tshut":        ["Dar Bharadwaja"],
    "Tulsi":        ["Deva Parashara"],
    "Tur":          ["Svamina Laugakshi"],
    "Turi":         ["Svamina Gotam Laugakshi"],
    "Turki":        ["Dar Bharadwaja"],
    "Ugra":         ["Datthtreya (Koul)"],
    "Ukhlu":        ["Dev Wasishta"],
    "Unt":          ["Pat Svamina Kaushika"],
    "Uthu":         ["Dar Bharadwaja"],
    "Vangar":       ["Dev Vishamitra Varshaganya"],
    "Vantu":        ["Bhava Kapishthala"],
    "Variku":       ["Bhava Aupamanyava"],
    "Vashnavi":     ["Pat Svamina Kaushika"],
    "Vichari":      ["Dar Bharadwaja"],
    "Waguzari":     ["Dar Bharadwaja"],
    "Wanikhan":     ["Bhava Kapishthal Aupamanyava"],
    "Wangani":      ["Kantha Dhaumyana Laugakshi Gautama"],
    "Wat":          ["Kantha Dhaumyana Laugakshi Gautama"],
    "Watal":        ["Pat Svamina Deva Ratra Parwara", "Svamina Kaushika"],
    "Waza":         ["Svamina Vas Atreya", "Pat Svamina Kaushika"],
    "Wufa":         ["Pat Svamina Kaushika"],
    "Yachh":        ["Deva Bharadwaja", "Deva Parashara"],
    "Yechh":        ["(Deva) Parashara"],
    "Zadu":         ["Bhava Kapishthala"],
    "Zahi":         ["Svamina Maudgalya"],
    "Zalpari":      ["Bhuta Was Aupamanyava Laugakshi"],
    "Zamindar":     ["Datthtreya (Koul)"],
    "Zari":         ["Kantha Dhaumyana Laugakshi Gautama", "Svamina Gautama"],
    "Zaru":         ["Deva Bharadwaja", "Rishi Kavigargya"],
    "Zitshoo":      ["Ratra Bhargava"],
    "Zitu":         ["Svamina Maudgalya"],
    "Zotan":        ["Svamina Maudgalya"],
}

GOTRAS = [
    "Kashyapa", "Vasishtha", "Vishwamitra", "Jamadagni", "Bharadwaja",
    "Atri", "Gautama", "Agastya", "Angirasa", "Bhrigu",
    "Kaushika", "Garga", "Shandilya", "Kaundinya", "Vatsya",
    "Harita", "Maudgalya", "Parashara", "Upamanyu", "Vatsa"
]

KUL_DEVIS = [
    "Sharika Devi (Hari Parbat)", "Jwala Devi (Khrew)", "Ragnya Devi (Tulamula)",
    "Bahuchara Mata", "Vaishno Devi (Trikuta Hills)", "Kheer Bhawani (Tulmul)",
    "Maha Kali (Barav)", "Durga Devi", "Saraswati Devi", "Tripura Sundari"
]

KUL_DEVTAS = [
    "Shiva (Amarnath)", "Vishnu (Martand)", "Surya (Martand)",
    "Ganesha", "Skanda", "Indra", "Kubera", "Varuna"
]

BHAIRAVAS = [
    "Kalabhairava", "Asitanga Bhairava", "Ruru Bhairava", "Chanda Bhairava",
    "Krodha Bhairava", "Unmatta Bhairava", "Kapala Bhairava", "Bhishana Bhairava",
    "Samhara Bhairava", "Swarna Akarshana Bhairava", "Batuka Bhairava"
]

# Nakshatra compatibility data for 36 Gunas
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

TITHI_NAMES = [
    "Pratipada", "Dwitiya", "Tritiya", "Chaturthi", "Panchami",
    "Shashthi", "Saptami", "Ashtami", "Navami", "Dashami",
    "Ekadashi", "Dwadashi", "Trayodashi", "Chaturdashi", "Purnima/Amavasya"
]

VARA_NAMES = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

YOGA_NAMES = [
    "Vishkambha", "Priti", "Ayushman", "Saubhagya", "Shobhana",
    "Atiganda", "Sukarma", "Dhriti", "Shula", "Ganda",
    "Vriddhi", "Dhruva", "Vyaghata", "Harshana", "Vajra",
    "Siddhi", "Vyatipata", "Variyana", "Parigha", "Shiva",
    "Siddha", "Sadhya", "Shubha", "Shukla", "Brahma",
    "Indra", "Vaidhriti"
]

KARANA_NAMES = [
    "Bava", "Balava", "Kaulava", "Taitila", "Garija",
    "Vanija", "Vishti", "Shakuni", "Chatushpada", "Naga",
    "Kimstughna"
]

RITU_NAMES = {
    (1, 2): "Vasanta (Spring)", (3, 4): "Grishma (Summer)",
    (5, 6): "Varsha (Monsoon)", (7, 8): "Sharad (Autumn)",
    (9, 10): "Hemanta (Pre-winter)", (11, 12): "Shishira (Winter)"
}

MASA_NAMES = [
    "Chaitra", "Vaishakha", "Jyeshtha", "Ashadha", "Shravana",
    "Bhadrapada", "Ashwina", "Kartika", "Margashirsha", "Pausha",
    "Magha", "Phalguna"
]

# Muhurats (auspicious times) data
INAUSPICIOUS_TIMES = {
    "Rahu Kaal": {0: (4.5, 6), 1: (7.5, 9), 2: (3, 4.5), 3: (6, 7.5), 
                   4: (1.5, 3), 5: (0, 1.5), 6: (9, 10.5)},  # in 1.5 hour slots from sunrise
}

