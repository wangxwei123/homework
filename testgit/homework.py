# 1、打印小猫爱吃鱼，小猫要喝水
# class Fish():
#     def __init__(self,fish):
#         self.fish=fish
#         # self.water=water
#     def print__info(self):
#         print(f'{self.fish}爱吃鱼,{self.fish}爱喝水')
# fish1 =Fish('小猫')
# fish1.print__info()

"""
2、小明爱跑步，爱吃东西。
1）小明体重75.0公斤
2）每次跑步会减肥0.5公斤
3）每次吃东西体重会增加1公斤
4）小美的体重是45.0公斤
"""
# class Health():
#     def __init__(self,weight,running,food):
#         self.weight = weight
#         self.running=running
#         self.food=food
#         self.free_weight=weight
#     def residual_weight(self,item):
#         if self.running=='跑':
#             if self.food =='无':
#                 self.free_weight = self.free_weight- 0.5
#             else:
#                 self.free_weight = self.free_weight + 0.5
#         elif self.running=='不跑步':
#             if self.food == '无':
#                 self.free_weight = self.free_weight
#             else:
#                 self.free_weight = self.free_weight + 1
#     def __str__(self):
#         return f'您的初始体重是{self.weight}公斤,今天是您是否跑步:{self.running},吃的东西是:{self.food},今天剩余体重是{self.free_weight}'
# xiaoming = Health(20,'不跑步','无')
# xiaoming.residual_weight(xiaoming)
# print(xiaoming)
"""""
需求：
1）.房子有户型，总面积和家具名称列表
   新房子没有任何的家具
2）.家具有名字和占地面积，其中
   床：占4平米
   衣柜：占2平面
   餐桌：占1.5平米
3）.将以上三件家具添加到房子中
4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表
"""""
class Furniture():
    def __init__(self,name,area):
        self.name=name
        self.area=area
class Home():
    def __init__(self,address,area):
        self.address=address
        self.area=area
        self.free_area=area
        self.furniture = []
    def __str__(self):
        return f'房子坐落于{self.address},占地面积{self.area},剩余面积{self.free_area},家具有{self.furniture}'
    def add_furiniture(self,item):
        if self.free_area>=item.area:
            self.furniture.append(item.name)
            self.free_area-=item.area
        else:
            print('家具太大，剩余面积不足，无法容纳')
bed =Furniture('双人床',4)
jia1 =Home('北京',1200)
# print(jia1)
wardrobe =Furniture('衣柜',2)
table=Furniture('餐桌',1.5)

jia1.add_furiniture(bed)
jia1.add_furiniture(wardrobe)
jia1.add_furiniture(table)
print(jia1)
