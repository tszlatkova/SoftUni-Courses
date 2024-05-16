# Шеф на компания забелязва че все повече служители прекарват  време в сайтове, които ги разсейват.
# За да предотврати това, той въвежда изненадващи проверки на отворените табове на браузъра на служителите си.
# Според отворения сайт в таба се налагат следните глоби:
# •	"Facebook" -> 150 лв.
# •	"Instagram" -> 100 лв.
# •	"Reddit" -> 50 лв.
# От конзолата се четат два реда:
# •	Брой отворени табове в браузъра n - цяло число в интервала [1...10]
# •	Заплата - число в интервала [500...1500]
# След това n – на брой пъти се чете име на уебсайт – текст
# Изход
# •	Ако по време на проверката заплатата стане по-малка или равна на 0 лева, на конзолата се изписва
# "You have lost your salary." и програмата приключва.
# •	В противен случай след проверката на конзолата се изписва остатъкът от заплатата (да се изпише като цяло число).

n = int(input())
salary = float(input())

for _ in range(n):
    site = input()
    if site == 'Facebook':
        salary -= 150
    elif site == 'Instagram':
        salary -= 100
    elif site == 'Reddit':
        salary -= 50
    else:
        continue

    if salary <= 0:
        print('You have lost your salary.')
        break

else:
    print(int(salary))

# if salary > 0:
#     print(int(salary))