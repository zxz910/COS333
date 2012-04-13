from posts.models import Thread, Post, Tag
from django.shortcuts import render_to_response, get_list_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# Return a list of the threads ordered by pub_date
def index(request):
	latest_thread_list = Thread.objects.all().order_by('-pub_date')
	return render_to_response('posts.html', {'thread_list': latest_thread_list},
								context_instance=RequestContext(request))
	
# Return the list of posts corresponding to thread with id thread_id,
# ordered by pub_date
def latest_posts(request, thread_id):
	posts = get_list_or_404(Post, thread = thread_id).order_by('-pub_date')
	return render_to_response('posts.html', {'latest_post_list': posts},
								context_instance=RequestContext(request))

def filter_threads(request):
	if (not request.POST.has_key('tags')):
		return index(request)
	tags_list =get_tags(request.POST['tags'])[1]
	if (not tags_list):
		return index(request)
	threads = list(Thread.objects.all())
	target_threads = []
	for thread in threads:
		temp1 = list(thread.tags.all())
		temp = []
		for t in temp1:
			temp.append(t.tag)
		if (list(set(temp) & set(tags_list))):
			target_threads.append(thread)
	return render_to_response('posts.html', {'thread_list': target_threads},
								context_instance=RequestContext(request))

def create_thread(request):
	tuple = get_tags(request.POST['title'])
	# Create and save new thread
	t = Thread(author=request.POST['author'], title=tuple[0], professor_viewable=(request.POST.has_key('professor_viewable')))
	t.save()
	for ttag in tuple[1]:
		tag = Tag(tag = ttag)
		tag.save()
		t.tags.add(tag)
	t.save()
	# Create and save new post
	p = Post(author=request.POST['author'], content=request.POST['content'], thread=t)
	p.save()
	return HttpResponseRedirect(reverse('posts.views.index'))
	
	
def post_comment(request):
	# Create and save new post
	p = Post(author=request.POST['author'], content=request.POST['content'], thread=Thread.objects.get(id=request.POST['thread']))
	p.save()
	return HttpResponseRedirect(reverse('posts.views.index'))
	
def get_tags(post):
	content = ''
	tags = []
	inTag = 0
	for i in range(0, len(post)):
		if inTag:
			if post[i] == ' ':
				inTag = 0
		elif post[i] == '#':
			tag = post[i:].split(' ')[0]
			tags.append(tag[1:])
			inTag = 1
		else:
			content += post[i]
	return (content, tags)
	