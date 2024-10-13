now = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))

t = end[0] * 3600 + end[1] * 60 + end[2] - (now[0] * 3600 + now[1]*60+now[2])

if t < 0 :
    t += 60*60*24
    
r_h =t//3600
r_m = (t%3600//60)
r_s = t%60

print("%02d:%02d:%02d" % (r_h, r_m, r_s))
    