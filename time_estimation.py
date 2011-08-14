#! /usr/bin/env python3

import cmd, sys, time

class EstimatorShell(cmd.Cmd):
	intro = 'Time estimation system.'
	prompt = '> '
	final = 100
	current = 0
	updates = []
	def do_final(self, arg):
		'Set the final quantity: final 100'
		arg = proc(arg)
		if len(arg)>0:
			self.final = arg[0]
			#print('Set the final quantity to %0.2f' % (self.final))
		else:
			print('Not enough arguments.')
		self.onecmd('status')
	def do_status(self, arg):
		'Print the current status: status'
		print('Finished %0.2f of %0.2f' % (self.current, self.final))
		if len(self.updates)<2:
			#print('Not enough data for completion time estimation.')
			pass
		else:
			rates = []
			for x in range(len(self.updates)-1):
				update1 = self.updates[x]
				update2 = self.updates[x+1]
				rates.append((update2[1]-update1[1])/(update2[0]-update1[0]))
			rate_mean = sum(rates) / len(rates)
			completion_mean = (self.final - self.current)/rate_mean
			completion_inst = (self.final - self.current)/rates[-1]
			print()
			print('Completion time based on mean rate (%0.2f n/s): %s' % (rate_mean,wordtime(completion_mean)))
			print('Completion time based on recent rate (%0.2f n/s): %s' % (rates[-1],wordtime(completion_inst)))
			print()
	def do_update(self, arg):
		'Updates the current state: current 50'
		arg = proc(arg)
		if len(arg)>0:
			self.current = arg[0]
			self.updates.append((time.time(),self.current))
			#print('Set the current to %0.2f' % (self.current))
		else:
			print('Not enough arguments.')
		self.onecmd('status')
	def do_increment(self, arg):
		'Increments the current state by a value (default 1): increment [delta]'
		arg = proc(arg)
		delta = 1
		if len(arg)>0:
			delta = arg[0]
		self.current += delta
		self.updates.append((time.time(),self.current))
		#print('Set the current to %0.2f' % (self.current))
		self.onecmd('status')
	def do_reset(self, arg):
		'Resets the updates and optionally sets the current state to the value (default 0): reset [current]'
		self.updates = []
		arg = proc(arg)
		if len(arg)>0:
			self.current = arg[0]
		else:
			self.current = 0
		self.onecmd('status')
	def do_exit(self, arg):
		'Exit the current session'
		sys.exit()

def proc(arg):
	arg = arg.split()
	ret = []
	for a in arg:
		try:
			ret.append(float(a))
		except ValueError:
			print('"%s" is not a valid number, skipping.' % (a))
	return ret
def wordtime(sec):
	ret = ''
	eta = time.time()+sec
	if sec >= 60*60*24:
		days = int(sec/(60*60*24))
		if days > 1:
			d = 'days'
		else:
			d = 'day'
		ret += '%d %s, '%(days,d)
		sec -= 60*60*24*days
	if sec >= 60*60:
		hours = int(sec/(60*60))
		if hours>1:
			h = 'hours'
		else:
			h = 'hour'
		ret += '%d %s, '%(hours,h)
		sec -= 60*60*hours
	if sec >= 60:
		minutes = int(sec/60)
		if minutes>1:
			m = 'minutes'
		else:
			m = 'minute'
		ret += '%d %s, '%(minutes,m)
		sec -= 60*minutes
	if sec > 0:
		if sec>1:
			s = 'seconds'
		else:
			s = 'second'
		ret += '%d %s'%(sec,s)
	ret = ret.strip(' ,')
	ret += ' ('+time.strftime('%m/%d/%y %H:%M:%S',time.localtime(eta))+')'
	return ret

if __name__ == '__main__':
	EstimatorShell().cmdloop()

