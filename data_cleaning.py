import pandas as pd
import io, re, sys
from os.path import join


def clean_data(path = ''):
	DS1 = join(path, 'data/PACCSS-IT.txt')
	DS2 = join(path, 'data/simpitiki-v2.xml')
	COLS = ['sentence_1', 'sentence_2']

	CSV_PARR_1 = {
		'on_bad_lines':'warn',
		'delimiter':'\t',
		'engine':'python',
		'quotechar':'§',
		'skipinitialspace':True,
		'decimal':'.'
	}


	def to_inmem_file(txt):
		f = io.StringIO()
		f.write(txt)
		f.seek(0)
		return f
		

	def clean_1(txt):
		# (!!!) Performed on raw data!
		txt = txt\
			.replace('"','')	\
			.replace("'",'')	\
			.replace("- ",'')	\
			.replace("  ",' ')	\
			.lower()
		#txt = re.sub('\d+[\./-]\d+[\./-]\d+', '<date>', txt)
		return txt


	def keep_inbetween(txt, tag):
		return re.sub(f'.*(<{tag}[^<>]*>.+</{tag}>).*', r'\1', txt, 0, re.DOTALL)
		

	def remove_tags(txt):
		'Remove tags; enclosed information is preserved.'
		return re.sub(f'</?[^<>]+>', lambda _:'', txt) if txt!=None else None
		

	# ----------- loading data -----------
	#print(pd.read_csv(DS1, **CSV_PARR_1).head(30))
	with open(DS1, 'r') as imf:
		txt = imf.read()

	inmem_DS1 = to_inmem_file(clean_1(txt))

	# ----------- loading data -----------
	with open(DS2, 'r') as imf2:
		txt = imf2.read()

	# ----------- creating DFs -----------
	df1 = pd.read_csv(inmem_DS1, usecols=COLS, **CSV_PARR_1)
	print(f'DF 1 has shape {df1.shape}')

	#legend = keep_inbetween(txt, 'types')
	#df_leg = pd.read_xml(to_inmem_file(legend), parser='etree')

	new_txt = keep_inbetween(txt, 'simplifications')
	df2 = pd.read_xml(to_inmem_file(new_txt), parser='etree')

	df2.drop(df2.columns[[0,1]], axis=1, inplace=True)
	df2.columns = COLS
	df2 = df2.applymap(remove_tags)
	print(f'DF 2 has shape {df2.shape}')

	combo = pd.concat([df1, df2], copy=False)

	return combo
