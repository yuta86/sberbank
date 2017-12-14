import csv
from .models import Banner, Category


def checkNoNone(str):
    if str != 'None':
        return True
    else:
        return False


def csv_dict_reader(filename):
    # categories = Category.objects.all()
    # print(categories)

    with open(filename, 'r') as csv_file:
        allRowList = csv.reader(csv_file, delimiter=';')
        next(allRowList)
        for currentRow in allRowList:
            i = 0
            url = ''
            for currentWorld in currentRow:
                i += 1
                if i == 1:  # 'Image URL'
                    print(i)
                    print(currentWorld)
                    url = currentWorld

                elif i == 2:  # 'shows'
                    print(i)
                    print(currentWorld)
                    shows = currentWorld
                    banner = Banner(url=url, shows=shows)
                    banner.save()
                    print("Добавил баннер")
                else:  # category
                    print(currentWorld)
                    if checkNoNone(currentWorld):
                        print('не равен None')
                        print('Добавляем')
                        c1 = Category.objects.filter(name=currentWorld)
                        # c2 = Category.objects.filter(name=currentWorld).values('id')
                        #
                        # print(c1)
                        # print(c2)
                        #
                        # c3 = list(c2)
                        # id = c3[0]['id']
                        # print(id)
                        if c1:
                            print("такая категория уже есть")
                            print(c1.values)
                            banner.category.add(c1)
                            # cat_temp = Category.objects.filter(id=id)
                        else:
                            # cat = Category.objects.create(name=currentWorld, description='')
                            cat = Category(name=currentWorld, description='')
                            cat.save()
                            print('ДОБАВИЛ в БД')
                            banner.category.add(cat)

    return True
