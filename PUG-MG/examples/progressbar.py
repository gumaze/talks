import sys, time

for i in range(100):
  sys.stdout.write('=')
  sys.stdout.flush()
  time.sleep(0.05)

sys.stdout.write('\n')
print('Pronto!')
