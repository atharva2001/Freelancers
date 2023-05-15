from collections import defaultdict
from django.shortcuts import redirect, render
from Forums.models import tags, forum, replies
from datetime import datetime
import copy
# Home Page of Forums
def index(request):
   content = {}
   db_forum = forum.objects.all()
   db_tag = tags.objects.all()

   if request.method == "POST":

      but = request.POST.get("submit")
      if but == "reply":
         print(request.session['id'])
         answer = request.POST.get("answer")
         author_name = request.POST.get("author_name")
         email = request.POST.get("email")
         image = request.FILES.get("image")
         rep = replies(forum_id=request.session['id'], author_name=author_name,
                       answer=answer,image=image)
         rep.save()
      else:

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
         'id' : i.id,
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

def read(request):
   if request.method == "POST":
      request.session['id'] = request.POST.get('id')
      form_content = {}
      reply_content = []
      forums = forum.objects.filter(id=request.session['id'])
      is_reply = replies.objects.filter(forum_id=request.session['id']).exists()
      reply = replies.objects.filter(forum_id=request.session['id'])
      for i in forums:
         form_content = {
            'email' : i.email,
            'title' : i.title,
            'tags' : i.tags,
            'name' : i.author_name,
            'desc' : i.description,
            'date' : i.date,
            'link' : "media/"+str(i.image)
         }
         if is_reply:
            for i in reply:
               temp = {
                  'name' : i.author_name,
                  'answer' : i.answer,
                  'date' : i.date,
                  'link' : "media/"+str(i.image)
               }
               # cp = copy.deepcopy(temp)
               reply_content.append(temp)
            
         # print(reply_content)

      
   return render(request, 'forums/read.html', {'content' : form_content, 'reply' : reply_content})
