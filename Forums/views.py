from collections import defaultdict
from django.shortcuts import redirect, render
from Forums.models import tags, forum, replies
from datetime import datetime

# Home Page of Forums
def index(request):
   content = {}
   db_forum = forum.objects.all()
   db_tag = tags.objects.all()

   if request.method == "POST":

      title = request.POST.get("title")
      tag = request.POST.get("tags")
      desc = request.POST.get("description")
      author_name = request.POST.get("author_name")
      email = request.POST.get("email")
      image = request.FILES.get("image")

      # temp_i = str(image).replace(" ", "_")
      # image = temp_i
      arr_tag = tag.split(",")

      temp_db_f = forum.objects.all().last()
      if temp_db_f != None:
         curr_f_id = temp_db_f.id + 1
      else:
         curr_f_id = 1

      for i in arr_tag:
         if tags.objects.filter(name=i.lower()).exists():
            temp_t = tags.objects.get(name=i)
            temp_t.content += "," + str(curr_f_id)
            temp_t.save()
         else:
            tg = tags(name=i.lower(), content=str(curr_f_id))
            tg.save()
      print(datetime.now())
      temp_f = forum(email=email, title=title, tags=tag, author_name=author_name, 
                     description=desc, date=datetime.now(), image=image)
      temp_f.save()

      




      

   
   for i in db_forum:
      content[i.id] = {
         'name' : i.author_name,
         'title' : i.title,
         'desc' : i.description,
         'tags' : i.tags,
         'date' : i.date,
         'link' : "media/"+str(i.image)
      }
   # print(content)

   '''
   content[id] = {
   data : asd
   ...
   }
   '''
   return render(request, 'forums/index.html', {'content' : content})

def add(request):
   return render(request, 'forums/editor.html')