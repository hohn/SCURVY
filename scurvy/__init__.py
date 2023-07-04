
# 
# Colors from https://colorbrewer2.org/?type=sequential&scheme=Blues&n=9.

# 
# The lightest from each have been removed.  
# 
colors=[
    # blues
    '#9ecae1','#6baed6','#4292c6','#2171b5','#08519c','#08306b',
    # greens
    '#a1d99b','#74c476','#41ab5d','#238b45','#006d2c','#00441b',
    # greys
    '#bdbdbd','#969696','#737373','#525252','#252525','#000000',
    # oranges
    '#fdae6b','#fd8d3c','#f16913','#d94801','#a63603','#7f2704',
    # purples
    '#bcbddc','#9e9ac8','#807dba','#6a51a3','#54278f','#3f007d',
    # reds
    '#fc9272','#fb6a4a','#ef3b2c','#cb181d','#a50f15','#67000d',
     ]

#
# To further enhance contrast, remove every other entry.
# 
colors2=[colors[i] for i in range(0, len(colors), 2)]
