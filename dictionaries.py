# Dictionaries, Learn Python - Full Course for Beginners [Tutorial]
monthConversions = {
    0: "January",  # Key and Value, 1 key for 1 value, can be int or str
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

# print(monthConversions["Dec"])
print(monthConversions.get(0, "Not a valid key"))  # A key and a default value
