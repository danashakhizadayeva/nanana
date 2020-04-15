from django.shortcuts import render
from .models import Video
from .models import theBase
from .models import numberOfVideos
#from .forms import VideoForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import random
from django.db import models
from os import listdir
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return render(request, 'polls/index.html')


def about(request):
    return render(request, 'polls/tmp.html', {'title': 'About'})


def database(request):
    context = {
        'signs': Sign.objects.all()
    }
    return render(request, 'polls/database.html', context, {'title': 'Database'})

randomText = int()

@login_required
def byhand(request):
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        #we got the file from web
        file = open('media/number-of-videos.txt', 'r+')
        content = file.read()
        new_number_of_videos = int(content) + 1
        #finding the number of videos (folders) that we have already in our media file
        fs = FileSystemStorage(location='media/'+str(new_number_of_videos))
        #allocating the file location to the new folder with the new number of videos
        file.truncate(0) 
        file.close
        file = open('media/number-of-videos.txt', 'w')
        file.write(str(new_number_of_videos))
        file.close
        #allocating new number of videos (folders to the existing text file)
        database_number = numberOfVideos.objects.get(name="number")
        database_number.number = str(new_number_of_videos)
        database_number.save()
        #allocating new number of videos in database



        global randomText
        #getting the sentence number from the global variable
        Sentence_number = randomText + 1
        filename = fs.save(str(Sentence_number) + '.webm', myfile)
        #video is saved

        theLocation = "media/" + str(new_number_of_videos)

        new_base = theBase(name="Base"+str(new_number_of_videos))
        new_base.save()
        new_base = theBase.objects.get(name="Base"+str(new_number_of_videos))
        the_user = User.objects.get(username=request.user.get_username())
        new_video_in_base = Video(name="Video"+str(new_number_of_videos),location=theLocation, text=Sentence_number, MLresults=new_base, user=the_user)
        new_video_in_base.save()
        #updating database



        uploaded_file_url = fs.url(filename)
        return render(request, 'polls/byhand.html', {
            'uploaded_file_url': uploaded_file_url}()
        )
    return render(request, 'polls/byhand.html', {'title': 'ByHand'})

#class myvideo(models.Model):
#    upload = models.FileField(upload_to='uploads/')


def mymytext(request):
    if request.method == 'GET':
        with open('texts.txt', 'r') as texts:
            array = []
            for line in texts:
                array.append(line)
        global randomText 
        randomText = random.randint(0,4)
        #assigning random number from 0 to number of sentences to the global random variable
        print (str(randomText))
        return HttpResponse(array[randomText], content_type='text/plain')
    return render(request, 'polls/byhand.html', {'title': 'ByHand'})


#def showvideo(request):

#    lastvideo = Video.objects.last()

#    videofile = lastvideo.videofile

#    form = VideoForm(request.POST or None, request.FILES or None)
#    if form.is_valid():
#        form.save()

#    context = {'videofile': videofile,
#               'form': form
#               }

#    return render(request, 'polls/index.html', context)


#def recordVideo(request):
#    return render(request, 'polls/recordVideo.html',  {'title': 'RecordVideo'})


#def add_movie_form_submission(request):
#    print("Hello form is submitted")
#    movie_name = request.POST["movie_name"]
#    movie_type = request.POST["movie_type"]
#    movie_review = request.POST["movie_review"]
#    movie_release_date = request.POST["movie_release_date"]
#    movie_detail = request.POST["movie_detail"]

#    movie_info = MovieInfo(movie_name=movie_name, movie_type=movie_type, movie_review=movie_review,
#                           movie_release_date=movie_release_date, movie_detail=movie_detail)

#    movie_info.save()
#    return render(request, 'polls/recordVideo.html')


def i(request):
    return render(request, 'polls/i.html')

@login_required
def bytyping(request):
    if request.method == 'POST':
        myfile = request.FILES['myfile']
        random_vid_path = str(randomVideo)
        path_to_folder = "media/" + random_vid_path + "/uploadedScreenshots/"
        fs = FileSystemStorage(location=path_to_folder)
        randomName = random.randint(0,100000)
        filename = fs.save(str(randomName) + '.png', myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'polls/bytyping.html', {
            'uploaded_file_url': uploaded_file_url}
        )
    return render(request, 'polls/bytyping.html')

randomVideo = int()


def video_access(request):
    if request.method == 'GET':
        file = open('media/number-of-videos.txt', 'r')
        content = file.read()
        file.close
        #getting the number of videos that we have
        global randomVideo
        randomVideo = random.randint(1,int(content))
        random_vid_path = str(randomVideo)
        #selecting one of the videos
        
        my_video = list_files1('media/'+ random_vid_path +'/', 'webm')
        my_video = list(my_video)
        mymyvideo ="" + my_video[0]
        path_to_video = "media/" + random_vid_path + "/" + mymyvideo
        return HttpResponse(path_to_video, content_type='text/plain')
        #returning the full path to our video
    return render(request, 'polls/bytyping.html')


def list_files1(directory, extension):
    return (f for f in listdir(directory) if f.endswith('.' + extension))


def image_access(request):
    if request.method == 'GET':
        global randomVideo
        file = open('media/' + str(randomVideo) + '/check.txt', 'r')
        content = file.read()
        file.close
        #getting the image numbers
        return HttpResponse(content, content_type='text/plain')
    return render(request, 'polls/bytyping.html')


def checkresults(request):
    if request.method == 'POST':
        mytext = request.body
        mytext = mytext.decode("utf-8")
        number_of_responses = (len(mytext)+1)/2
        i = 0
        global randomVideo
        the_base = theBase.objects.get(name="Base"+str(randomVideo))
        #print(type(request.user.get_username()))
        if the_base.usersprovided is None:
            the_base.usersprovided = request.user.get_username() + " "
        else:
            the_base.usersprovided = the_base.usersprovided + request.user.get_username() + " "

        while (i < number_of_responses):
            if (i == 0):
                the_base.check1 = the_base.check1 + mytext[0] + " "
            elif (i == 1):
                the_base.check2 = the_base.check2 + mytext[2] + " "
            elif (i == 2):
                the_base.check3 = the_base.check3 + mytext[4] + " "
            elif (i == 3):
                the_base.check4 = the_base.check4 + mytext[6] + " "
            elif (i == 4):
                the_base.check5 = the_base.check5 + mytext[8] + " "
            elif (i == 5):
                the_base.check6 = the_base.check6 + mytext[10] + " "
            elif (i == 6):
                the_base.check7 = the_base.check7 + mytext[12] + " "
            elif (i == 7):
                the_base.check8 = the_base.check8 + mytext[14] + " "
            elif (i == 8):
                the_base.check9 = the_base.check9 + mytext[16] + " "
            elif (i == 9):
                the_base.check10 = the_base.check10 + mytext[18] + " "
            elif (i == 10):
                the_base.check11 = the_base.check11 + mytext[20] + " "
            
            i = i + 1

        the_base.save()
        return render(request, 'polls/bytyping.html')        
    return render(request, 'polls/bytyping.html')