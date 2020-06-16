from datetime import datetime
class Rectangular():
    def __init__(self, x, y, width, height,time=None):
        """
        description: 
            difine a rectangular in X-Y coordinate
        args:
            x: horizontal coordinate
            y: vertical coordinate 
            width: the segment between x, x+ width 
            height: the segment between y, y+height
            time: timeStamp of the creation of this object
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.area = width * height
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
        self.time = dt_string

    def filter_accepted_rectangular(self, others):
        """
        description: 
            Select thoses rectangular that has intersection with main rectangular
        args:
            Take a instace of Rectangular Class
        Return: 
            List of dictionay of accepted Rectangular
        """
        accepted_list = []
        for item in others:
            if self._has_ratio(item):
                accepted_list.append(item.json_able())
        return accepted_list

    def _has_ratio(self, other):

        #indicting which one in the right or left
        if self.x <= other.x:
            self.left_rect = self
            self.right_rect = other
        else:
            self.left_rect = other
            self.right_rect = self

        #indicting which one in the top or bottom 
        if self.y  >= other.y:
            self.top_rect = self
            self.bottom_rect = other
        else:
            self.top_rect = other
            self.bottom_rect = self
        
        #calculating overlap width
        #No overlap
        if self.left_rect.x + self.left_rect.width <= self.right_rect.x:
            self.overlap_width = 0

        #fully overlap
        elif (self.left_rect.x + self.left_rect.width) >= (self.right_rect.x+self.right_rect.width):
            self.overlap_width =  self.right_rect.width

        #partialy overlap
        else:
            self.overlap_width = (self.left_rect.x + self.left_rect.width) - self.right_rect.x 
        
        #==========================================================#
        #==========================================================#
        
        #calculating overlap height
        #No overlap
        if self.bottom_rect.y + self.bottom_rect.height <= self.top_rect.y :
            self.overlap_height = 0

        #fully overlap
        elif (self.bottom_rect.y + self.bottom_rect.height) >= (self.top_rect.y+self.top_rect.height):
            self.overlap_height =  self.right_rect.height

        #partialy overlap
        else:
            self.overlap_height = (self.bottom_rect.y + self.bottom_rect.height) - self.top_rect.y
        
        # print(self.area)
        # print(other.area)
        # print(30*"#")
        # print(self.overlap_width)
        # print(self.overlap_height)
        if self.overlap_width > 0 and self.overlap_height > 0:
            self.intersection_area = self.overlap_width * self.overlap_height / self.area
            other.intersection_area = self.overlap_width * self.overlap_height / self.area 
            # print("product",self.overlap_width * self.overlap_height)        
            return self.intersection_area
        else:
            return None
    
    def json_able(self):
        """
        description: 
            it return just a dictionary of class attributes
        """
        
        ret = {"x":self.x, "y":self.y, "width":self.width,
                "height":self.height,"ratio":self.intersection_area,"time":self.time}
        return ret

if __name__ == "__main__":
    r1 = Rectangular(0,0,10,20)
    r2 = Rectangular(2,18,5,4)
    r3 = Rectangular(12,18,5,4)
    r4 = Rectangular(-1,-1,5,4)
    r5 = Rectangular(3,2,5,10)
    r6 = Rectangular(4,10,1,1)
    r7 = Rectangular(9,10,5,4)
    area11 = r1._has_ratio(r1)
    area12 = r1._has_ratio(r2)
    area13 = r1._has_ratio(r3)
    area14 = r1._has_ratio(r4)
    area56 = r5._has_ratio(r6) 
    area57 = r5._has_ratio(r7)
    for i in [area11,area12,area13,area14,area56,area57]:
        if i :
            print(i)






# class Rectangular():
#     def __init__(self, x, y, width, height,time=None):
#         """
#         description: 
#             difine a rectangular in X-Y coordinate
#         args:
#             x: horizontal coordinate
#             y: vertical coordinate 
#             width: the segment between x, x+ width 
#             height: the segment between y, y+height
#             time: timeStamp of the creation of this object
#         """
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height

#         now = datetime.now()
#         dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
#         self.time = dt_string
    
#     def _has_intersection(self,other):
#         """
#         description: 
#             Check that the intersection of two objects(Intersection is symmetric).
#             if just of vertex in second rectangular in main rectangular 
#             then they have an intersection.
#             WARNING: this definition excludes the boundary.
#         args:
#             Take a instace of Rectangular Class
#         Return(boolen): 
#             True if there exist a intersection Area
#         """

#         x1 = (self.x < other.x < (self.x+ self.width)) 
#         x2 = (self.x < (other.x + other.width) < (self.x+ self.width))
#         y1 = (self.y < other.y < (self.y + self.height))
#         y2 = (self.y < (other.y + other.height) < (self.y + self.height))
#         #these are four boolean that indcate the existence of vertices in main rectangular 
#         x1y1 = (x1 and y1)
#         x2y1 = (x2 and y1)
#         x1y2 = (x1 and y2)
#         x2y2 = (x2 and y2)
#         if any([x1y1, x2y1, x1y2, x2y2]):
#             return True
#         return False

#     def filter_accepted_rectangular(self, others):
#         """
#         description: 
#             Select thoses rectangular that has intersection with main rectangular
#         args:
#             Take a instace of Rectangular Class
#         Return: 
#             List of dictionay of accepted Rectangular
#         """
#         accepted_list = []
#         for item in others:
#             if self._has_intersection(item):
#                 accepted_list.append(item.json_able())
#         return accepted_list
    
#     def json_able(self):
#         """
#         description: 
#             it return just a dictionary of class attributes
#         """
        
#         ret = {"x":self.x, "y":self.y, "width":self.width, "height":self.height,"time":self.time}
#         return ret