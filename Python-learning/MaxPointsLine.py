# http://oj.leetcode.com/problems/max-points-on-a-line/
# Max Points on a Line
# Given n points on a 2D plane, 
# find the maximum number of points 
# that lie on the same straight line.

# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points) <= 1:
            return len(points)
        glob_dict = {}
        glob_dict['self'] = 1
        for i in range(0,len(points)):
            local_dict = {}
            local_dict['self'] = 1
            for j in range(i+1,len(points)):
                #print points[j].x, points[i].x, points[j].y, points[i].y, points[j]==points[i]
                if points[j].x == points[i].x and points[j].y == points[i].y:
                    local_dict['self'] += 1 
                    continue
                if points[j].x - points[i].x == 0:
                    if 'infinity' not in local_dict:
                        local_dict['infinity'] = 1
                    else:
                        local_dict['infinity'] += 1
                else:
                    slope = float(points[j].y - points[i].y)/(points[j].x - points[i].x)
                    if slope not in local_dict:
                        local_dict[slope] = 1
                    else:
                        local_dict[slope] += 1

            #print 'local_dict', local_dict
            #print 'base', local_dict['self']

            for key in local_dict:
                if key in glob_dict:
                    if key == 'self':
                        if(glob_dict[key] < local_dict[key]):
                            glob_dict[key] = local_dict[key]
                    elif glob_dict[key] < local_dict[key] + local_dict['self']:
                        glob_dict[key] = local_dict[key] + local_dict['self']
                else:
                    glob_dict[key] = local_dict[key] + local_dict['self']
        max_num = 0
        for key in glob_dict:
            if glob_dict[key] > max_num:
                max_num = glob_dict[key]
        #print '----', glob_dict
        return max_num # plus the point itself



        
#import MaxPointsLine
points =  [Point(0,0)]
points.append(Point(1,1))
points.append(Point(0,0))
#points.append(Point(2,3))
#points.append(Point(2,6))
#points.append(Point(2,5))
#points.append(Point(2,4))
#print points
s = Solution()
print 'result', s.maxPoints(points)


