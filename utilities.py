def memoization(limit):
	MEM = dict()
	# decorator:
	def memoizza__(f):
		def g(*x):
			nonlocal MEM, limit
			if x in MEM: return MEM[x]
			else:
				res = f(*x)
				if len(MEM)>=limit and limit!=0:
					MEM.popitem() # bad for top-down procedures!
				MEM[x] = res
				# print(MEM)
				return res
		return g
	return memoizza__
	

class Translator:
	def __init__(self, word_to_idx, idx_to_word, tokenizer, flat_default=False, fun=lambda _:_):
		self.w2i = word_to_idx
		self.i2w = idx_to_word
		self.tk = tokenizer
		self.flat = flat_default
		self.f = fun	

	def tr(self, what, flat=None):
		if flat is None:
			flat=self.flat
		if isinstance(what, str):
			tr = [self.w2i[token] for token in self.tk(what)]
			return self.f(tr) if flat else self.f([tr])
		else:
			tr = [self.i2w[token] for token in (what if flat else what[0])]
			return ' '.join(tr)
			
def resize(perc):
	from IPython.display import display, HTML
	display(HTML("<style>.container { width:"+str(perc)+"% !important; }</style>"))
	
	

def plot_trend(data_x, data_y, x_lab='x', y_lab='y', title='', lines=True, regress=True, figsize=(15,6), line_style='-o'):
	from scipy.stats import linregress
	import matplotlib.pyplot as plt
	plt.figure(figsize=figsize)
	plt.margins(0)
	plt.plot(data_x, data_y, line_style, linewidth=1, markersize=10)
	min_ , max_ = plt.ylim()
	rg = max_ - min_
	plt.xlabel(x_lab, fontsize=18)
	plt.xticks(data_x if len(data_x)<figsize[0] else [data_x[0]]+[_ for i,_ in enumerate(data_x) if i%int(len(data_x)/figsize[0])==0]+[data_x[-1]])
	if lines:
		for i,_ in enumerate(data_x): plt.axvline(_, color='gray', linestyle=":", ymax=(data_y[i]-min_)/rg)
	if regress:
		lr_res = linregress(data_x, data_y)
		y = lr_res.intercept + lr_res.slope*data_x
		plt.plot([data_x[0], data_x[-1]] , [y[0], y[-1]], 'r')
		plt.plot([0, data_x[-1]], [y[-1], y[-1]], color='gray', linestyle='--')
	plt.ylabel(y_lab, fontsize=18)
	if title: plt.title(title, fontsize=18)
	plt.show()


