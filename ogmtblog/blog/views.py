from django.shortcuts import redirect, render,  HttpResponse, get_object_or_404
from django.contrib import messages
from blog.models import Post, blogComment
from django.urls import reverse





# Create your views here.
def blogpage(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, "blog/blogpage.html", context)
    # return HttpResponse("  This is a Blog Pge . we will start posting soon so stay")

def blogpost(request, slug):
    # post = Post.objects.filter(slug=slug)
    post = get_object_or_404(Post, slug=slug)
    comments = blogComment.objects.filter(post=post)
    context = {"post": post, 'comments': comments}
    return render(request, "blog/blogpost.html", context)
#     # return HttpResponse("This is the Blog Post : {slug}")

def postComment(request):
    if request.method == 'POST':

        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to post a comment.")
            # Redirect to login page with the next parameter to return to the current page after login
            return redirect(f"/userlogin?next={request.POST.get('postSno')}")

        comment=request.POST.get('comment')
        user=request.user
        postSno=request.POST.get('postSno')
        # post=Post.objects.get(sno=postSno)
        post = get_object_or_404(Post, sno=postSno)
        parentSno=request.POST.get('parentSno')
    #     if parentSno == "":
    #         comment=blogComment(comment=comment, user=user, post=post)
    #         comment.save()
    #         messages.success(request, "Yout comment has been posted successfully")
    #     else:
    #         parent=blogComment.objects.get(sno=parentSno)
    #         comment=blogComment(comment=comment, user=user, post=post, parent=parent)
    #         comment.save()
    #         messages.success(request, "Yout reply has been posted successfully")
    
    # return redirect(f"/blog/{post.slug}")



        if parentSno:
            parent = get_object_or_404(blogComment, sno=parentSno)
            comment_instance = blogComment(comment=comment, user=user, post=post, parent=parent)
        else:
            comment_instance = blogComment(comment=comment, user=user, post=post)
        
        comment_instance.save()
        messages.success(request, "Your comment has been posted successfully")

        return redirect(f"/blog/{post.slug}")

    return redirect('/blog/')


