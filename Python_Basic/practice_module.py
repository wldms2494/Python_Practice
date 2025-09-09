import theater_module as mv
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# 다 안적을래..
# multi cursor : ctrl + alt + shift + 방향키
# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)


# 군인 함수는 알려주지마  !
# from theater_module import price, price_morning
# price(3)
# price_morning(4)
# price_soldier(5)

from theater_module import price_soldier as price
price(5) # 군인 가격 