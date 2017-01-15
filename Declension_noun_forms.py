# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 08:56:21 2017

@author:sourabh
"""

a_stem_masculine=[['अः','औ','आः'],
              ['अम्','औ','आन्'],
              ['एन','आभ्याम्','ऐः'],
              ['आय','आभ्याम्','एभ्यः'],
              ['आत्','आभ्याम्','एभ्यः'],
              ['अस्य','अयोः','आनाम्'],
              ['ए','अयोः','एषु'],
              ['अ','औ','आः']]
        
i_stem_masculine=[['इः','ई','अयः'],
              ['इम्','ई','ईन्'],
              ['इना','इभ्याम्','इभिः'],
              ['अये','इभ्याम्','इभ्यः'],
              ['एः','इभ्याम्','इभ्यः'],
              ['एः','योः','ईनाम्'],
              ['औ','योः','इषु'],
              ['ए','ई','अयः']]
              
u_stem_masculine=[['उः','ऊ','अवः'],
              ['उम्','ऊ','ऊन्'],
              ['उना','उभ्याम्','उभिः'],
              ['अवे','उभ्याम्','उभ्यः'],
              ['ओः','उभ्याम्','उभ्यः'],
              ['ओः','वोः','ऊनाम्'],
              ['औ','वोः','उषु'],
              ['ओ','ऊ','अवः']]
             
r_stem_masculine_1=[['आ','अरौ','अरः'],
                  ['अरम्','अरौ','ऋन्'],
                  ['रा','ऋभ्याम्','ऋभिः'],
                  ['रे','ऋभ्याम्','ऋभ्यः'],
                  ['उः','ऋभ्याम्','ऋभ्यः'],
                  ['उः','रोः','ऋणाम्'],
                  ['अरि','रोः','ऋषु'],
                  ['अः','अरौ','अरः']]
                  
r_stem_masculine_2=[['आ','अारौ','अारः'],
                  ['अारम्','अारौ','ऋन्'],
                  ['रा','ऋभ्याम्','ऋभिः'],
                  ['रे','ऋभ्याम्','ऋभ्यः'],
                  ['उः','ऋभ्याम्','ऋभ्यः'],
                  ['उः','रोः','ऋणाम्'],
                  ['अरि','रोः','ऋषु'],
                  ['अः','अरौ','अरः']]
                
o_stem_masculine=[['औः','आवौ','आवः'],
                 ['आम्','आवौ','आः'],
                 ['अवा','ओभ्याम्','ओभिः'],
                 ['अवे','ओभ्याम्','ओभ्यः'],
                 ['ओः','ओभ्याम्','ओभ्यः'],
                 ['ओः','अवोः','अवाम्'],
                 ['अवि','अवोः','ओषु'],
                 ['औः' 'आवौ' 'आवः']]
t_stem_masculine_1=[['आन्','अन्तौ','अन्तः'],
                    ['अन्तम्','अन्तौ','अतः'],
                    ['अता','अद्भ्याम्','अद्भिः'],
                    ['अते','अद्भ्याम्','अद्भ्यः'],
                    ['अतः','अद्भ्याम्','अद्भ्यः'],
                    ['अतः','अतोः','अताम्'],
                    ['अति','अतोः','अत्सु'],
                    ['अन्','अन्तौ','अन्तः']]
                    
t_stem_masculine_2=[['अन्','अन्तौ','अन्तः'],
                    ['अन्तम्','अन्तौ','अतः'],
                    ['अता','अद्भ्याम्','अद्भिः'],
                    ['अते','अद्भ्याम्','अद्भ्यः'],
                    ['अतः','अद्भ्याम्','अद्भ्यः'],
                    ['अतः','अतोः','अताम्'],
                    ['अति','अतोः','अत्सु'],
                    ['अन्','अन्तौ','अन्तः']]
                    
t_stem_masculine_3=[['अत्','अतौ','अतः'],
                    ['अतम्','अतौ','अतः'],
                    ['अता','अद्भ्याम्','अद्भिः'],
                    ['अते','अद्भ्याम्','अद्भ्यः'],
                    ['अतः','अद्भ्याम्','अद्भ्यः'],
                    ['अतः','अतोः','अताम्'],
                    ['अति','अतोः','अत्सु'],
                    ['अत्','अतौ','अतः']]
c_stem_masculine=[['अक्','अचौ','अचः'],
                  ['अचम्','अचौ','अचः'],
                  ['अचा','अग्भ्याम्','अग्भिः'],
                  ['अचे','अग्भ्याम्','अग्भः'],
                  ['अचः','अग्भ्याम्','अग्भः'],
                  ['अचः','अचोः','अचाम्'],
                  ['अच्','अचोः','अक्षु'],
                  ['अक्','अचौ','अचः']]   
                 
j_stem_masculine=[['अज्','अजौ','अजः'],
                  ['अजम्','अजौ','अजः'],
                  ['अजा','अग्भ्याम्','अग्भिः'],
                  ['अजे','अग्भ्याम्','अग्भः'],
                  ['अजः','अग्भ्याम्','अग्भः'],
                  ['अजः','अजोः','अजाम्'],
                  ['अजि','अजोः','अक्षु'],
                  ['अज्','अजौ','अजः']]



en_stem_masculine=[['ई','इनौ','इनः'],
                   ['इनम्','इनौ','इनः'],
                   ['इना','इभ्याम्','इभिः'],
                   ['इने','इभ्याम्','इभ्यः'],
                   ['इनः','इभ्याम्','इभ्यः'],
                   ['इनः','इनोः','इनाम्'],
                   ['इनि','इनोः','इषु'],
                   ['इन्','इनौ','इनः']]

n_stem_masculine_1=[['आ','आनौ','आनः'],
                    ['आनम्','आनौ','नः'],
                    ['ना','अभ्याम्','अभिः'],
                    ['ने','अभ्याम्','अभ्यः'],
                    ['नः','अभ्याम्','अभ्यः'],
                    ['नः','नोः','नाम्'],
                    ['नि','नोः','असु'],
                    ['अन्','आनौ','अानः']]

n_stem_masculine_2=[['आ','आनौ','आनः'],
                    ['आनम्','आनौ','अनः'],
                    ['अना','अभ्याम्','अभिः'],
                    ['अने','अभ्याम्','अभ्यः'],
                    ['अनः','अभ्याम्','अभ्यः'],
                    ['अनः','अनोः','अनाम्'],
                    ['अनि','अनोः','असु'],
                    ['अन्','आनौ','अानः']]
                 
a_stem_feminine=[['आ','ए','आः'],
                 ['आम्','ए','आः'],
                 ['अया','आभ्याम्','आभिः'],
                 ['आयै','आभ्याम्','आभ्यः'],
                 ['आयाः','आभ्याम्','आभ्यः'],
                 ['आयाः','अयोः','आनाम्'],
                 ['आयाम्','अयोः','आसु'],
                 ['ए','ए', 'आः']]
                 
i_stem_feminine=[['इः','ई','अयः'],
                ['इम्','ई','ईः'],
                ['या','इभ्याम्','इभिः'],
                ['यै','इभ्याम्','इभ्यः'],
                ['याः','इभ्याम्','इभ्यः'],
                ['याः','योः','ईनाम्'],
                ['याम्','योः','इषु'],
                ['ए','ई','अयः']]
                
ii_stem_feminine=[['ई','यौः','यः'],
                 ['ईम्','यौः','ईः'],
                 ['या', 'ईभ्याम्','ईभिः'],
                 ['यै','ईभ्याम्','ईभ्यः'],
                 ['याः','ईभ्याम्','ईभ्यः'],
                 ['याः','योः','ईनाम्'],
                 ['याम्','योः','ईषु'],
                 ['इ','यौ','यः']]

u_stem_feminine=[['उः','ऊ','अवः'],
                 ['उम्','ऊ','ऊः'],
                 ['वा','उभ्याम्','उभिः'],
                 ['वै','उभ्याम्','उभ्यः'],
                 ['वाः','उभ्याम्','उभ्यः'],
                 ['वाः','वोः','ऊनाम्'],
                 ['वाम्','वोः','उषु'],
                 ['ओ','ऊ','अवः']]
                 
uu_stem_feminine=[['ऊः','वौ','वः'],
                  ['ऊम्','वौ','ऊः'],
                  ['वा','ऊभ्याम्','ऊभिः'],
                  ['वै','ऊभ्याम्','ऊभ्यः'],
                  ['वाः','ऊभ्याम्','ऊभ्यः'],
                  ['वाः','वोः','ऊनाम्'],
                  ['वाम्','वोः','ऊषु'],
                  ['उ','वौ','वः']]
                  
r_stem_feminine=[['आ','अरौ','अरः'],
                 ['अरम्','अरौ','ऋः'],
                 ['रा','ऋभ्याम्','ऋभिः'],
                 ['रे','ऋभ्याम्','ऋभ्यः'],
                 ['उः','ऋभ्याम्','ऋभ्यः'],
                 ['उः','रोः','ऋृणाम्'],
                 ['अरि','रोः','ऋषु'],
                 ['अः','अरौ','अरः']]
                 
oo_stem_feminine=[['औः','आवौ','आवः'],
                  ['आवम्','आवौ','आवः'],
                  ['आवा','औभ्याम्','औभिः'],
                  ['आवे','औभ्याम्','औभ्यः'],
                  ['आवः','औभ्याम्','औभ्यः'],
                  ['आवः','आवोः','आवाम्'],
                  ['आवि','आवोः','औषु'],
                  ['औः','आवौ','आवः']]  
                  
c_stem_feminine=[['अक्-ग्','अचौ','अचः'],
                 ['अचम्','अचौ','अचः'],
                 ['अचा','अग्भ्याम्','अग्भिः'],
                 ['अचे','अग्भ्याम्','अग्भ्यः'],
                 ['अचः','अग्भ्याम्','अग्भ्यः'],
                 ['अचः','अचोः','अचाम्'],
                 ['अचि','अचोः','अक्षु'],
                 ['अक्-ग्','अचौ','अचः']]
                 
t_stem_feminine=[['त','अतौ','अतः'],
                 ['अतम्','अतौ','अतः'],
                 ['अता','दभ्याम्','दभिः'],
                 ['अते','दभ्याम्','दभ्यः'],
                 ['अतः','दभ्याम्','दभ्यः'],
                 ['अतः','अतोः','अताम्'],
                 ['अति','अतोः','तसु'],
                 ['त','अतौ','अतः']]
                 
sh_stem_feminine=[['अक्-ग्','अशौ','अशः'],
                 ['अशम्','अशौ','अशः'],
                 ['अशा','अग्भ्याम्','अग्भिः'],
                 ['अशे','अग्भ्याम्','अग्भ्यः'],
                 ['अशः','अग्भ्याम्','अग्भ्यः'],
                 ['अशः','अशोः','अशाम्'],
                 ['अशि','अशोः','अक्षु'],
                 ['अक्-ग्','अशौ','अशः']]
                 
h_stem_feminine=[['अत्','अहौ','अहः'],
                 ['अहम्','अहौ','अहः'],
                 ['अहा',' अद्भ्याम्','अद्भिः'],
                 ['अहे','अद्भ्याम्','अद्भ्यः'],
                 ['अहः','अद्भ्याम्','अद्भ्यः'],
                 ['अहः','अहोः','अहाम्'],
                 ['अहि','अहोः','अत्सु'],
                 ['अत्','अहौ','अहः']]
           
dh_stem_feminine=[['अत्','अधौ','अधः'],
                 ['अधम्','अधौ','अधः'],
                 ['अधा','द्भ्याम्','द्भिः'],
                 ['अधे','द्भ्याम्','द्भ्यः'],
                 ['अधः','द्भ्याम्','द्भ्यः'],
                 ['अधः','अधोः','अधाम्'],
                 ['अधि','अधोः','त्सु'],
                 ['अत्','अधौ','अधः']]
                 
d_stem_feminine=[['अत्','अदौ','अदः'],
                 ['अदम्','अदौ','अदः'],
                 ['अदा','अद्भ्याम्','अद्भिः'],
                 ['अदे','अद्भ्याम्','अद्भ्यः'],
                 ['अदः','अद्भ्याम्','अद्भ्यः'],
                 ['अदः','अदोः','अदाम्'],
                 ['अदि','अदोः','अत्सु'],
                 ['अत्','अदौ','अदः']]
a_stem_neuter=[['अम्','ए','आनि'],
                ['अम्','ए','आनि'],
                ['एन','आभ्याम्','ऐः'],
                ['आय','आभ्याम्','एभ्यः'],
                ['आत्','आभ्याम्','एभ्यः'],
                ['अस्य','अयोः','आनाम्'],
                ['ए','अयोः','एषु'],
                ['अ','औ','आः']]
                
i_stem_neuter_1=[['इ','इनी','ईनि'],
                 ['इ','इनी','ईनि'],
                 ['इना','इभ्याम्','इभिः'],
                 ['इने','इभ्याम्','इभ्यः'],
                 ['इनः','इभ्याम्','इभ्यः'],
                 ['इनः','इनोः','ईनाम्'],
                 ['इनि','इनोः','इषु'],
                 ['इ',',इनी','ईनि']]
                 
i_stem_neuter_2=[['इ','इनी','ईनि'],
                 ['इ','इनी','ईनि'],
                 ['ना','इभ्याम्','इभिः'],
                 ['ने','इभ्याम्','इभ्यः'],
                 ['नः','इभ्याम्','इभ्यः'],
                 ['नः','नोः','नाम्'],
                 ['नि','नोः','इषु'],
                 ['इ','इनी','ईनि']]
                 
u_stem_neuter=[['उ','उनी','ऊनि'],
               ['उ','उनी','ऊनि'],
               ['उना','उभ्याम्','उभिः'],
               ['उने','उभ्याम्','उभ्यः'],
               ['उनः','उभ्याम्','उभ्यः'],
               ['उनः','उनोः','ऊनाम्'],
               ['उनि','उनोः','उषु'],
               ['उ','उनी','ऊनि']]
               
s_stem_neuter=[['अः','असी','आंसि'],
               ['अः','असी','आंसि'],
               ['असा','ओभ्याम्','ओभिः'],
               ['असे','ओभ्याम्','ओभ्यः'],
               ['असः','ओभ्याम्','ओभ्यः'],
               ['असः','असोः','असाम्'],
               ['असि','असोः','अःसु'],
               ['अः','असी','आंसि']]
               
n_stem_neuter=[['अ','अनी','आनि'],
               ['अ','अनी','आनि'],
               ['ना','अभ्याम्','अभिः'],
               ['ने','अभ्याम्','अभ्यः'],
               ['नः','अभ्याम्','अभ्यः'],
               ['नः','नोः','नाम्'],
               ['नि','नोः','असु'],
               ['अ','अनी','आनि']]
               
t_stem_neuter=[['अत्','अती','अन्ति'],
               ['अत्','अती','अन्ति'],
               ['अता','अद्भ्याम्','अद्भिः'],
               ['अते','अद्भ्याम्','अद्भ्यः'],
               ['अतः','अद्भ्याम्','अद्भ्यः'],
               ['अतः','अतोः','अताम्'],
               ['अति','अतोः','अत्सु'],
               ['अत्','अती','अन्ति']]

सम्राज्=[['सम्राट्','सम्राजौ','सन्राजः'],
      ['सम्राजम्','सम्राजौ','सम्राजः'],
      ['सम्राजा','सम्राड्भ्याम्','सम्राड्भिः'],
      ['सम्राजे','सम्राड्भ्याम्','सम्राड्भ्यः'],
      ['सम्राजः','सम्राड्भ्याम्','सम्राड्भ्यः'],
      ['सम्राजः','सम्राजोः','सम्राजाम्'],
      ['सम्राजि','सम्राजोः','सम्राट्सु'],
      ['सम्राट्','सम्राजौ','सम्राजः']]
      
पथिन्=[['पन्थाः','पन्थानौ','पन्थानः'],
       ['पन्थानम्','पन्थानौ','पथः'],
       ['पथा','पथिभ्याम्','पथिभिः'],
       ['पथे','पथिभ्याम्','पथिभ्यः'],
       ['पथः','पथिभ्याम्','पथिभ्यः'],
       ['पथः','पथोः','पथाम्'],
       ['पथि','पथोः','पथिषु'],
       ['पन्थाः','पन्थानौ','पन्थानः']]
       
       
विद्वस्=[['विद्वान्','विद्वांसौ','विद्वासः'],
         ['विद्वासम्','विद्वांसौ','विदुषः'],
         ['विदुषा','विद्वद्भ्याम्','विद्वद्भिः'],
         ['विदुषे','विद्वद्भ्याम्','विद्वद्भ्यः'],
         ['विदुषः','विद्वद्भ्याम्','विद्वद्भ्यः'],
         ['विदुषः','विदुषोः','विदुषाम्'],
         ['विदुषि','विदुषोः','विद्वत्सु'],
         ['विद्वन्','विद्वांसौ','विद्वासः']]
         
स्त्री=[['स्त्री','स्त्रियौ','स्त्रियः'],
    ['स्त्रियम्','स्त्रियौ','स्त्रियः'],
    ['स्त्रिया','स्त्रीभ्याम्','स्त्रीभिः'],
    ['स्त्रियै','स्त्रीभ्याम्','स्त्रीभ्यः'],
    ['स्त्रियाः','स्त्रीभ्याम्','स्त्रीभ्यः'],
    ['स्त्रियाः','स्त्रियोः','स्त्रीणाम्'],
    ['स्त्रियाम्','स्त्रियोः','स्त्रीषु'],
    ['स्त्री','स्त्रियौ','स्त्रियः']]
              
all_D_forms=[a_stem_masculine,i_stem_masculine,u_stem_masculine,r_stem_masculine_1,r_stem_masculine_2,o_stem_masculine,
          a_stem_feminine,i_stem_feminine,ii_stem_feminine,u_stem_feminine,uu_stem_feminine,r_stem_feminine,oo_stem_feminine,
          t_stem_feminine,c_stem_feminine,h_stem_feminine,dh_stem_feminine,d_stem_feminine,sh_stem_feminine,a_stem_neuter,
          i_stem_neuter_1,i_stem_neuter_2,u_stem_neuter,en_stem_masculine,t_stem_masculine_1,t_stem_masculine_2,t_stem_masculine_3,
          n_stem_masculine_1,n_stem_masculine_2,c_stem_masculine,j_stem_masculine,
          t_stem_neuter,s_stem_neuter,n_stem_neuter]
dict_forms={0:'a_stem_masculine',
           1:'i_stem_masculine',
           2:'u_stem_masculine',
           3:'r_stem_masculine_1',
           4:'r_stem_masculine_2',
           5:'o_stem_masculine',
           6:'a_stem_feminine',
           7:'i_stem_feminine',
           8:'ii_stem_feminine',
           9:'u_stem_feminine',
           10:'uu_stem_feminine',
           11:'r_stem_feminine',
           12:'oo_stem_feminine',
           13:'a_stem_neuter',
           14:'i_stem_neuter_1',
           15:'i_stem_neuter_2',
           16:'u_stem_neuter',
           17:'en_stem_masculine',
           18:'t_stem_masculine_1',
           19:'t_stem_masculine_2',
           20:'t_stem_masculine_3',
           21:'n_stem_masculine_1',
           22:'n_stem_masculine_2',
           23:'c_stem_masculine',
           24:'j_stem_masculine',
           25:'t_stem_feminine',
           26:'c_stem_feminine',
           27:'h_stem_feminine',
           28:'dh_stem_feminine',
           29:'d_stem_feminine',
           30:'sh_stem_feminine',
           31:'t_stem_neuter',
           32:'s_stem_neuter',
           33:'n_stem_neuter'}
