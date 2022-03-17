import dataframe_image as dfi

# Function that saves a df as an image
def saves_png(df, img_name, path):
	dfi.export(df, f'{path}{img_name}.png', table_conversion='matplotlib')

# Function that groups a df and sumarizes by sum
def groupby_sum(df, cols_names, cols_sum):
	return df.groupby(cols_names, as_index=False)[[cols_sum]].sum()

