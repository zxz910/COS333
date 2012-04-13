from posts.models import Thread, Post, Tag
from django.shortcuts import render_to_response, get_list_or 404

# Return a list of the threads ordered by pub_date
def latest_threadIndex(request):
	latest_thread_list = Thread.objects.all().order_by('-pub_date')
	return render_to_response(, {'latest_thread_list': latest_thread_list})
	
# Return the list of posts corresponding to thread with id thread_id,
# ordered by pub_date
def latest_posts(request, thread_id):
	posts = get_list_or_404(Post, thread = thread_id).order_by('-pub_date')
	return render_to_response(, {'latest_post_list': posts})

def get_threads_by_tags(request, tags_list):
	threads = list(Thread.objects.all())
	target_threads = []
	for (thread in Thread.objects.all()):
		temp = list(thread.tag_set)
		if (list(set(temp) & set(tags_list))):
			target_threads.append(thread)
	return render_to_response(, {'threads_by_tag_list': target_threads})

def create_thread(request):
	p = Thread(author=request.POST['author'], title=request.POST['title'], professor_viewable=request.POST['professor_viewable'])