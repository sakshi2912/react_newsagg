from .models import Lead,covid1,technews
from .serializers import *
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import *
import requests
from bs4 import BeautifulSoup
import re

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

class technewsView(generics.ListCreateAPIView):
    
    r9 = requests.get("https://www.indiatoday.in/technology/news")
    soups = BeautifulSoup(r9.content, 'html5lib')
    ht_headings = soups.findAll("div", {"class": "detail"})
    templist1=[]
    templist2=[]
    templist3=[]
    templistg=[]
    templista=[]
    for i in ht_headings:
        for j in i.find_all("h2"):
            for link in j.find_all('a'):
                if link.has_attr('href'):
                    templist1.append(link.attrs['href'])
    for i in templist1:
        string='https://www.indiatoday.in/'
        string=string+i
        templist3.append(string)
        string=""
    for i in ht_headings:
        for j in i.find_all('h2'):
            templist2.append(j.text)

    for i in ht_headings:
        for j in i.find_all('p'):
            templistg.append(j.text)
        
    for i in templistg:
            regex=re.compile(r'[\n\r\t]')
            i= regex.sub("",i)
            templista.append(i)

    newlist=[list(x) for x in zip(templista,templist3)]
    newdicta=dict(zip(templist2,newlist))
    


    r21 = requests.get("https://tech.economictimes.indiatimes.com/latest-news")
    soup1 = BeautifulSoup(r21.content, 'html5lib')
    ht_headings1 = soup1.findAll("div", {"class": "desc"})
    templistb1=[]
    templistl1=[]
    templistk1=[]
    templistg1=[]
    templista1=[]
    for i in ht_headings1:
        for j in i.find_all("h2"):
            for link in j.find_all('a'):
                if link.has_attr('href'):
                    templistb1.append(link.attrs['href'])

    for i in ht_headings1:
        for j in i.find_all('h2'):
            templistl1.append(j.text)
        for k in i.find_all('p'):
            templistg1.append(k.text)
    print(templistg1)
    for i in templistg1:
            regex=re.compile(r'[\n\r\t]')
            i= regex.sub("",i)
            templista1.append(i)
    newlista1=[list(x) for x in zip(templista1,templistb1)]
    newdicta1=dict(zip(templista1,newlista1))
    
    #print(newdicta1)
    ndtv_tech = requests.get("https://gadgets.ndtv.com/")
    soup_ndtv_tech = BeautifulSoup(ndtv_tech.content, 'html5lib')
    trending_techa1=[]
    links_techa1=[]
    head_techa1=soup_ndtv_tech.find_all("div",{"class":"nlist bigimglist"})
    for title in head_techa1:
        for x in title.find_all('a'):
            if x.has_attr('href'):
                links_techa1.append(x.attrs['href'])
                for di in x.find_all('div',{"class":'caption'}):
                    trending_techa1.append(di.text)
    
    ndtv_trenda1=dict(zip(trending_techa1,links_techa1))

    tech_full ={}
    tech_full['Economic Times']=newdicta1
    tech_full['India Today']=newdicta
    source = []
    head = []
    desc = []
    linklist = []
    for i,j in tech_full.items():
	    for key,value in j.items():
                source.append(i)
                head.append(key)
                desc.append(value[0])
                linklist.append(value[1])
    technews.objects.all().delete()
    
    for i in range(0,len(source)):
	    x = technews(headlines = head[i],description = desc[i], hyperlink =linklist[i], source = source[i] )
	    x.save()
    queryset = technews.objects.all()
    serializer_class = technewsSerializer


class weathernewsView(generics.ListCreateAPIView):

    #city_name=request.POST.get('num1',"Bangalore")
    city_name="Bangalore"
    api_key = "3ad2ac3e95c4efef9655dc196435a52c"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(url)
    x = response.json()
    list1q=[]
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]  
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        list1q.append(city_name)
        list1q.append(int(int(current_temperature)-273.15))  
        list1q.append(current_pressure)
        list1q.append(current_humidiy)
        list1q.append(weather_description)
    else:
        list1q=[]
    weatherdetails.objects.all().delete()
    for i in range(0,len(list1q)):
        x = weatherdetails(city = list1q[0],temperature =  list1q[1],pressure = list1q[2], humidity =  list1q[3],description=list1q[4] )
        x.save()
    queryset = weatherdetails.objects.all()
    serializer_class=weathernewsSerializer


class fullmoreView(generics.ListCreateAPIView):

    r1 = requests.get("https://www.hindustantimes.com/india-news/")
    r2 = requests.get("https://timesofindia.indiatimes.com/briefs")
    r3 = requests.get("https://www.newsbtc.com/")



    ht_soup = BeautifulSoup(r1.content, 'html5lib')
    toi_soup = BeautifulSoup(r2.content, 'html5lib')
    cryp_soup = BeautifulSoup(r3.content, 'html5lib')

    ht_headlines = []
    ht_headcontent=[]
    templista=[]
    templistb=[]

    ht_headings = ht_soup.findAll("div", {"class": "media-heading headingfour"})
    ht_links = ht_soup("a", {"class":"title"})


    for i in ht_headings:
        for link in i.find_all('a'):
            if link.has_attr('href'):
                templistb.append(link.attrs['href'])  
            
    for i in ht_headings:
        for c in ht_links:
            ht_headlines.append(c[title])
        
    for hth in ht_headings:
        ht_headlines.append(hth.text)

    for news in ht_soup.find_all('div', attrs={'class': 'media-body'}):
        for c in news.find_all('p'):
            ht_headcontent.append(c.text)
    #print(len(ht_headings),len(ht_headcontent),len(templistb))


    ht_cont_link=[list(x) for x in zip(ht_headcontent,templistb)]

    newsdict=dict(zip(ht_headlines,ht_cont_link))

    for i in newsdict:
        regex=re.compile(r'[\n\r\t]')
        if(i.startswith("\n\t\t\t\t")):
            i= regex.sub("",i)
            templista.append(i)
            
        else:
            pass
        
    ht_full_dict=dict(zip(templista,ht_cont_link))
   

    #times of india


    toi_headings = toi_soup.find_all('h2')
    toi_headings = toi_headings[0:-13] 

    templistc=[]
    templistd=[]
    templiste=[]
    templistf=[]
    newsdivs=toi_soup.find_all('div', attrs={'class': 'brief_box'})
    toi_headings = toi_soup.find_all('h2')
    for foo in newsdivs:
        for data in foo.find_all('p'):
            templistc.append((data.text))
            
    toi_news = []

    for th in toi_headings:
        toi_news.append(th.text)

    for i in newsdivs:
        for link in i.find_all('a'):
            if link.has_attr('href'):
                templistd.append(link.attrs['href'])
            
    for i in range(0,len(templistd),3):
        if(not(templistd[i].startswith('/briefs'))):
            templiste.append(templistd[i])
        
    
    
    for i in templiste:
        string='https://timesofindia.indiatimes.com'
        string=string+i
        templistf.append(string)
        string=""
        
    new_lst = [list(x) for x in zip(templistc,templistf)]

    toi_full_dict=dict(zip(toi_news,new_lst))
    x_list = []
    f_list =[]
    new_toi = []
    
    for i in templistc:
        i = i.replace('\'','’')
        i = i.replace('"','’’')
        x_list.append(i)
    for i in templistf:
        i = i.replace('\'','’')
        i = i.replace('"','’’')
        f_list.append(i)

    for i in toi_news:
        i = i.replace('\'','’')
        i = i.replace('"','’’')
        new_toi.append(i)


    templistg=[]
    templisth=[]
    templisti=[]
    headings = cryp_soup.find_all("h2",{"class": "title medium"})
    last_a_tag = cryp_soup.findAll("h2", {"class": "title medium"})
    for i in last_a_tag:
        for link in i.find_all('a'):
            if link.has_attr('href'):
                templisti.append(link.attrs['href'])
         
    for new in headings:
        for newdata in new.find_all("a"):
            templisth.append(newdata.text)
    newsDivs = cryp_soup.findAll("article")
    for c in newsDivs:       
            for data in c.find_all('p'):
                    templistg.append(data.text)
            
    newlist=[list(x) for x in zip(templistg,templisti)]
    crypt_full_dict=dict(zip(templisth,newlist))
    full_dict={}
    full_dict['Times Of India']=toi_full_dict
    full_dict['Hindustan TImes']=ht_full_dict
    full_dict['BTC news']=crypt_full_dict

    source = []
    head = []
    desc = []
    linklist = []
    for i,j in full_dict.items():
	    for key,value in j.items():
                source.append(i)
                head.append(key)
                desc.append(value[0])
                linklist.append(value[1])
    fullmore.objects.all().delete()

    for i in range(0,len(source)):
	    x = fullmore(headlines = head[i],description = desc[i], hyperlink =linklist[i], source = source[i] )
	    x.save()
    queryset = fullmore.objects.all()
    serializer_class = fullmoreSerializer


class sportsnewsView(generics.ListCreateAPIView):

    ht_r = requests.get("https://www.hindustantimes.com/sports-news/")
    list21=[]
    list22=[]
    list23=[]
    list24=[]
    ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
    ht_headings = ht_soup.findAll("div", {"class": "media-heading headingfour"})
    links = ht_soup("a", {"class":"title"})
    for i in ht_headings:
        for link in i.find_all('a'):
            if link.has_attr('href'):
                list24.append(link.attrs['href']) 
    for i in ht_headings:
        for c in links:
            list23.append(c[title])
            
    for hth in ht_headings:
        list23.append(hth.text)
    #print(list23)
    for news in ht_soup.find_all('div', attrs={'class': 'media-body'}):
        for c in news.find_all('p'):
            list22.append(c.text)
            
    newlist=[list(x) for x in zip(list22,list24)]
    newsdict=dict(zip(list23,newlist))
    for i in newsdict:
        regex=re.compile(r'[\n\r\t]')
        if(i.startswith("\n\t\t\t\t")):
            i= regex.sub("",i)
            list21.append(i)
            
        else:
            pass
        
    newssports=dict(zip(list21,newlist))

    sport_r = requests.get("https://www.sportspundit.com/cricket/articles/?gclid=Cj0KCQjwpfHzBRCiARIsAHHzyZrKzHfccihdgUuRCL5ZtKJ_9kBeZlUgopM9oTvPtfpo6zGuTGDDyNYaAiSTEALw_wcB")
    list25=[]
    list27=[]
    list26=[]
    list28=[]
    list29=[]
    list30=[]
    list31=[]
    list32=[]
    ht_soup = BeautifulSoup(sport_r.content, 'html5lib')
    ht_headings = ht_soup.findAll("div", {"class": "text-holder","id":"articles"})
    #ht_headings1 = ht_soup.find_all("h2")
    for i in ht_headings:
        for data in i.find_all('h2'):
            list27.append((data.text))
    for i in ht_headings:
        for data in i.find_all('p'):
            list26.append((data.text))
    for i in ht_headings:
        for data in i.find_all('h2'):
            for link in data.find_all('a'):
                if link.has_attr('href'):
                    list28.append(link.attrs['href']) 

    for i in list27:
        regex=re.compile(r'[\n\r\t]')
        if(i.startswith("\n")):
            i= regex.sub("",i)
            list31.append(i)
            
        else:
            pass

    for i in list26:
        regex=re.compile(r'[\n\r\t]')
        if(i.startswith("\n")):
            i= regex.sub("",i)
            list32.append(i)
            
        else:
            pass
    
    for i in list28:
        string='https://www.sportspundit.com'
        string=string+i
        list29.append(string)
        string=""
    newlist=[list(x) for x in zip(list32,list29)]

    newssports1=dict(zip(list31,newlist))

    #############indianexpress sports news
    list41=[]
    list42=[]
    list43=[]
    list44=[]
    list45=[]
    ht_r = requests.get("https://indianexpress.com/section/sports/")
    ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
    ht_headings = ht_soup.findAll("div", {"class": "articles"})

    for i in ht_headings:
        for data in i.find_all("h2"):
            list41.append(data.text)
    for i in ht_headings:
        for data in i.find_all("h2"):
            for link in data.find_all('a'):
                if link.has_attr('href'):
                    list42.append(link.attrs['href'])

    for i in ht_headings:
        for data in i.find_all('p'):
            list43.append(data.text)
            
    for i in list41:
        regex=re.compile(r'[\n\r\t]')
        if(i.startswith("\n\t\t\t\t\t\t\t")):
            i= regex.sub("",i)
            list44.append(i)
            
        else:
            pass

    for i in list43:
            regex=re.compile(r'[\n\r\t]')
    
            i= regex.sub("",i)
            list45.append(i)
            

    newlist=[list(x) for x in zip(list45,list42)]

    newssports2=dict(zip(list44,newlist))

    items1={}
    items1["Hindustan Times"]=newssports
    items1["Sportspundit"]=newssports1
    items1["IndianExpress"]=newssports2

    source = []
    head = []
    desc = []
    linklist = []
    for i,j in items1.items():
	    for key,value in j.items():
                source.append(i)
                head.append(key)
                desc.append(value[0])
                linklist.append(value[1])
    sportsnews.objects.all().delete()
    for i in range(0,len(source)):
	    x = sportsnews(headlines = head[i],description = desc[i], hyperlink =linklist[i], source = source[i] )
	    x.save()
    queryset= sportsnews.objects.all()
    serializer_class = sportsnewsSerializer




class worldnewsView(generics.ListCreateAPIView):
    templistl=[]
    templistm=[]
    templistn=[]
    r4 = requests.get("https://www.ndtv.com/world-news")
    soup_ndtv = BeautifulSoup(r4.content, 'html5lib')
    title=soup_ndtv.find("div",{"class":"ins_left_rhs"})
    for item in title.find_all("li"):
        for divi in item.find_all("div",{"class":"new_storylising_contentwrap"}):
            for anch in divi.find_all("a"):
                if anch.has_attr('title'):
                    templistm.append(anch.attrs['title'])
                if anch.has_attr('href'):
                    templistn.append(anch.attrs['href'])
            for dis in divi.find_all("div",{"class":"nstory_intro"}):
                templistl.append(dis.text)

    ndtv_dict={}        
    newlist_ndtv=[list(x) for x in zip(templistl,templistn)]

    ndtv_dict=dict(zip(templistm,newlist_ndtv))
    
    list5a=[]
    list5b=[]
    list5c=[]
    
    ht_ra = requests.get("https://economictimes.indiatimes.com/news/international/world-news")
    ht_soupa = BeautifulSoup(ht_ra.content, 'html5lib')
    headings = ht_soupa.find_all("div", {"class":"eachStory"})
    for i in headings:
        for data in i.find("h3"):
            list5a.append(data.text)
        for cont in i.find_all("p"):
            list5b.append(cont.text)
        for link in i.find_all("a"):
            if link.has_attr('href'):
                list5c.append('https://economictimes.indiatimes.com'+link.attrs['href'])

    newlist_it=[list(x) for x in zip(list5b,list5c)]
    inddict=dict(zip(list5a,newlist_it))


    templistj=[]
    templistk=[]
    head=soup_ndtv.find_all("div",{"class":"description"})
    for title in head:
        for x in title.find_all('a'):
            templistj.append(x.text)
            if x.has_attr('href'):
                templistk.append(x.attrs['href'])
    ndtv_trend=dict(zip(templistj,templistk))        
    #print(trend)
            


    world={}
    world['Economic Times']=inddict
    world['NDTV']=ndtv_dict
    
    source = []
    head = []
    desc = []
    linklist = []
    for i,j in world.items():
	    for key,value in j.items():
                source.append(i)
                head.append(key)
                desc.append(value[0])
                linklist.append(value[1])
    worldnews.objects.all().delete()

    for i in range(0,len(source)):
	    x = worldnews(headlines = head[i],description = desc[i], hyperlink =linklist[i], source = source[i] )
	    x.save()
    queryset= worldnews.objects.all()
    serializer_class = worldnewsSerializer


class covid1View(generics.ListCreateAPIView):  
        list51=[]
        list52=[]
        list53=[]
        list54=[]
        ht_r = requests.get("https://www.hindustantimes.com/")
        ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
        ht_headings = ht_soup.findAll("div", {"class": "widget-inner loadable","id":"election0"})
        ht_headings2 = ht_soup.findAll("div", {"class": "widget-inner loadable","id":"election1"})
        ht_headings1 = ht_soup.findAll("a", {"class":"fll-covrge"})
        for i in ht_headings:
            for link in i.find_all('a'):
                    if link.has_attr('href'):
                        list52.append(link.attrs['href'])

        for i in ht_headings1:
            for link in i.findAll("ul",{"id":"t2"}): 
                for k in link.find_all("span"):
                        list53.append((k.text))

        for i in ht_headings1:
            for link in i.findAll("ul",{"id":"t1"}):
                for k in link.find_all("span"):
                        list53.append((k.text))

        for i in list52:
            list53.append(i)


        covid1.objects.all().delete()
        covidlist = []
        for i in range(len(list53)):
            if i%2 != 0 :
                covidlist.append(list53[i])
        x = covid1(place = 'WORLD',number = covidlist[0])
        x.save()
        x = covid1(place = 'INDIA',number = covidlist[1])
        x.save()

        queryset = covid1.objects.all()
        serializer_class = covid1Serializer 

class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        posts_serializer = PostSerializer(data=request.data)
        if posts_serializer.is_valid():
            posts_serializer.save()
            return Response(posts_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', posts_serializer.errors)
            return Response(posts_serializer.errors, status=status.HTTP_400_BAD_REQUEST)