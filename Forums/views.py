from collections import defaultdict
from django.shortcuts import redirect, render
from Forums.models import tags, forum, replies

# Home Page of Forums
def index(request):
   tag = tags.objects.all()
   forums = forum.objects.all()
   # reply = replies.objects.get()
   hashmap = {}
   tagging = {}
   for i in tag:
      hashmap[i.id] = []
      tagging[i.id] = i

   for i in forums:
      arr = i.tags.split(',')
      for j in arr:
         hashmap[int(j)].append(i)

   content = {}
   for k in hashmap:
      for i in hashmap[k]:
         date = str(i.date)
         dt = date.split(' ')[0]
         # print()

         if i.id not in content:
            content[i.id] = [
               {
                  'tags' : tagging[k], 
                  'name' : i.author_name, 
                  'title' : i.title, 
                  'link' : "media/"+str(i.image),
                  'desc' : i.description,
                  'date' : dt.split('-')[2] + "-" + dt.split('-')[1] + "-" + dt.split('-')[0]
                  }
               ]
   # print(content)


   return render(request, 'forums/index.html', {'content' : content})

def add(request):
   return render(request, 'forums/editor.html')