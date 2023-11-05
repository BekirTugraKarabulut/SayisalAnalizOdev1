import math

i=math.pi/5
j=math.cos(i)
k=math.cos(0)

KesmeHatasıBulmaTek = j - k

print("\n<- Taylor Serisin de pi/5 in tek ve iki terimli durumlarda kesme hatasını bulma ->\n")

print("***Taylor Serisi Tek Terimli Kesme Hatası Bulma***\n")
print(KesmeHatasıBulmaTek)

m = (math.cos(0)) - (math.sin(0) * (i - 0)) - (math.cos(0) * (i * i ) / 2)

KesmeHatasıBulmaİkili = j - m

print("\n")

print("***Taylor Serisi İki Terimli Kesme Hatası Bulma***\n")
print(KesmeHatasıBulmaİkili)

print("\n")