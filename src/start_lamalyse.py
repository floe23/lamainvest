from manager.lamalyse import Lamalyse

analyser = Lamalyse()
analyser.debug = True
data = analyser.start('NBEV')
print("successfully updated analyse")
