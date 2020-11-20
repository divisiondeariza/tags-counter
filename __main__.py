from scraper import TagCounter, Tabulator

if __name__ == "__main__":
    print("""
****************************************************,.......********************
**************************************************,...........,*****************
********************************##(***********,,. /*. .   . ....,***************
*******************,,,,*********#((((((/**.,#. ,##(. ,(/. ,/((##(,.,************
******,************,**,,****,,,,(#(//***. (#%#(((#(((,  /(#(*.       ,****/*****
******,***********,,*,,,****,,,,/#(//**,.%#%#(#*. ./(((%##//#(#####(   ,/*******
******,/#(((******,***,,,***,,,,*((//**,%#%#%/(%%,(//(%#%#((/**/%###%../(((((#**
******,,(((//*******,,,*****,,,,,((//*/%##%##(###((((%%###(((, *&####( ,*//(#(**
*****,**(((/(/,,,,,,,****,,,,,,.... ./#########((((#%%####/(((/(/.####.,*//(/***
****/(((((((((/************,..........(*,#%####((((%######((((########.,*//* .**
*,####((**/////*********,............ ((*,  .(##((########(((#(#####(/,*//,  ..*
%%#((#((((,,//*/**,**,...........  . .,#(/,     #(,#####(/(((##(/,***       ....
(##(((/(/**(//////,..............      .#((*    .,,,/*.,,#*     *//,         ...
((##(((/*//**/(//**,,.  ...... ..    .   ,##(*   .,,,,,,     .///*           ...
##((////(%&&&%%%(. ,,,,,,,.,..  ... ..    %###((/, ,      *((//,              ..
%&&&%%&%(*         ,,,***,,,,,,,,,,,,   .&&.  ./(((//(//////.                 .,
#.                 ,******,,,,,,,,.     ,%%/                                  .,
                   .*******,,,,.           *(%%%%####%%%#                .,,,***
.                  ********,             #%%%#%#%#%#####/                   .,**
,,                 ,***.                 #%#%#%#%%######.                       
..                                       .     (#%#####(                        
,..                                           .%#######.                        
.,..,                                         /#######(                         
,,,, ..                          .            ########*                         
..,,,.,.,                     ..             (#####((((##.                      
....,..*....           .*,* .    ..         .%#####(((#(#(#(&%.                 
...,,,,,,.. ,. .... . .,/,..,,*. .          *######(( ,(##((&&#                 
...,,.,,,**... . .  ,*../ ..,.. **       ./(########, /##(((&&(                 
.....,....,* ,,, .. . . ,,**. .       #(#((######(((((((((/#%%                  
...../(,,.*.,,.,,....   .  .,*.,,      *((//*/(#((((((((/(/&&,                  
((,,,..,//,/,,/(,,..  . ....,,,,         *#(((((((((((//(/%&,                   
,((,.*,,/(..**,*.,,,* . .  ,...                 .    ,/(/%&/         


*** Welcome to the tags counter, let's count some html Tags! ***
    """)
    url = input("Please enter an URL:  ")
    tag_counter = TagCounter(url)
    tabulator = Tabulator()
    print("this page has {} tags".format(tag_counter.count_total_tags()))
    print("the top 5 tags are:")
    print(tabulator.generate(tag_counter.get_top_used_tags()))


