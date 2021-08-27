# -*- coding:utf-8 -*-

def rayCasting(point, Polygons):
    px = point['x']
    py = point['y']
    flag = False

    idx = 0
    lPolygon = len(Polygons)
    end = lPolygon - 1
    # for(idx = 0, l = Polygons.length, j = l - 1; idx < l; j = idx, idx++):
    while idx < lPolygon:
        sx = Polygons[idx]['x']
        sy = Polygons[idx]['y']
        tx = Polygons[end]['x']
        ty = Polygons[end]['y']

        # 点与多边形顶点重合
        if (sx == px and sy == py) or (tx == px and ty == py):
            return px, py

        # 判断线段两端点是否在射线两侧
        if (sy < py <= ty) or (sy >= py > ty):
            # 线段上与射线 Y 坐标相同的点的 X 坐标
            x = sx + (py - sy) * (tx - sx) / (ty - sy)
            # 点在多边形的边上
            if x == px:
                return px, py
            # 射线穿过多边形的边界
            if x > px:
                flag = not flag
        end = idx
        idx += 1

    # 射线穿过多边形边界的次数为奇数时点在多边形内
    return (px, py) if flag else 'out'


# 根据数组下标奇偶数得到点的坐标
def GetPoint(Str):
    idx = 0
    XYCoord = []
    while idx < len(Str.split(',')[1::2]):
        XYCoord.append({'x': float(Str.split(',')[::2][idx]),
                        'y': float(Str.split(',')[1::2][idx])})
        idx += 1
    return XYCoord


# 根据输入的点循环判断芝麻是否在多边形里面，如果全部在外面则输出no,否则输出芝麻的坐标
def metafunction(totalPoints, totalPolygons):
    count = 0
    for Point in totalPoints:
        rs = rayCasting(Point, totalPolygons)
        if rs == 'out':
            count += 1
        else:
            print(rs)

    if count == len(totalPoints):
        print("no")


if __name__ == '__main__':
    zhima = "6,4,8,8,9,9"
    duobianxing = "1,1,7,3,5,7"

    Points = GetPoint(zhima)
    Polygon = GetPoint(duobianxing)
    metafunction(Points, Polygon)
