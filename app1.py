
from flask import Flask, render_template, request
import config
import blog
import requests


def page_not_found(e):
  return render_template('404.html'), 404

app=Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)
@app. route('/',methods =['GET','POST'])
def index():
   if request.method == 'POST':
      if 'form1' in request.form:
         user_selection=request.form.getlist('blog_section')
         user_answer=request.form.get('blog_topics') 
         if(not user_selection):
           if (not user_answer):
            Blogexpanderresult=''
            prompt1 = request.form['blogTopic']
            blogT = blog.generateBlogTopics(prompt1)
            blogT = blogT.split("\n")
            blogT=list(filter(None,blogT))
            blog3=[]
            for blog1 in blogT:
               blog2="<input type='radio' name='blog_topics' style='margin-right: -2px' value='"+blog1+"'>"
               blog1=blog2+"<label for'"+blog1+"'>"+blog1+"</label><br>"
               blog3.append(blog1)
            blogTopicIdeas=' '.join(map(str,blog3))
            image_url  = blog.BlogTopicImage(prompt1)
            BlogImage = image_url.replace('\n','<br>')
           else:
            blogT = blog.generateBlogSection(user_answer)
            blogT=blogT.split("\n")
            blogT=list(filter(None,blogT))
            blog3=[]
            for blog1 in blogT:
               blog2="<input type='checkbox' name='blog_section'  value='"+blog1+"'onclick=''>"
               blog1=blog2+"<label for'"+blog1+"'>"+blog1+"</label><br>"
               blog3.append(blog1)
            blogSectionIdeas = ' '.join(map(str,blog3))
            blogTopicIdeas=''
            user_answer=''
         else:
            blogSectionIdeas=''
            Blogexpander=[]
            for i in user_selection:
               blogT = blog.BlogSectionExpander(i)
               blogexpand=blogT.replace('\n','<br>')
               Blogexpander.append(blogexpand)
            Blogexpanderresult=' '.join(map(str,Blogexpander))
            #img = Image.open(requests.get(image_url, stream=True).raw)
            #tk_img = ImageTk.PhotoImage(img)
            #BlogImage = tk_img.replace('\n','<br>')

                  
   return render_template('index.html', **locals())
if __name__ == '__main_':
   app.run(host='0.0.0.0', port='8888', debug=True)