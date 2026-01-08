st = "Sun rises In East"

# print(len(st))
# print(st.lower())
# print(st.casefold())
# print(st.upper())
# print(st.capitalize())
# print(st.title())
# print(st.strip())
# print(st.replace('s','K'))
# print(st.find("East"))
# print(st.startswith("Sun"))
# print(st.endswith("ß"))
# print("*****************************************")
# print(st.split(" ",-1))
# print(st.join("--"))
# print("abc".isalpha())
# print("123wq".isdigit())
# print("and123@".isalnum())
# print("abc".zfill(15))
# print("$$$".center(50,"*"))


# k = "hellopythonhellotops"

# print(k[0:7])
# print(k[5:9])
# print(k[6:])
# print(k[1:17:3])
# print(k[-1])
# print(k[::-1])

# print("*****************************************")

words = st.split(" ")
for w in words:
    print(w[::-1],end=" ")