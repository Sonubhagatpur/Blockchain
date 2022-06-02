import hashlib
def hashGenerater(data):
	result=hashlib.sha256(data.encode())
	return result

class Block:
	def __init__(self,data,hash,prev_hash):
	      self.data=data
	      self.hash=hash
	      self.prev_hash=prev_hash
	      
class Blockchain():
	def __init__(self):
		hashLast=hashGenerater('gen_last')
		hashStart=hashGenerater('gen_hash')
		
		genesis=Block('gen-data',hashStart,hashLast)
		self.chain=[genesis]
		
		def add_block(self,data):
			prev_hash=self.chain[-1].hash
			hash=hashGenerater(data+prev_hash)
			block=Block(data,hash,prev_hash)
			self.chain.append(block)
		
bc=Blockchain()
bc.block('1')
bc.add_block('2')
bc.add_block('3')
for block in bc.chain:
	print(block.__dict__)
