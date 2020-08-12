import arrow
print(arrow.utcnow().to('local').format('YY-MM-DD HH:mm:ss'))
#for item in range(1,32):
#    print('第'+str(item)+'次')