from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from .forms import SignUpForm, LoginForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json

def geterrorResponse(form):
    if form._errors:
        errors = {}
        errors['status'] = 'error'
        errors['messages'] = form._errors
        return errors

# Create your views here.
@csrf_exempt
def register(request: HttpRequest):
    if request.method == 'POST':
        requestDict = json.loads(request.body)
        form = SignUpForm(requestDict)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            user.refresh_from_db()
            raw_password = form.cleaned_data.get('password1')
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            user = authenticate(request, username=user.username, password=raw_password)
            if user is not None:
                login(request, user)

                return HttpResponse(json.dumps({'message':'congrats', 'pk':user.pk}))

        else:
            return HttpResponse(json.dumps(geterrorResponse(form)))
            # current_site = get_current_site(request)
            # subject = 'Activate Your MySite Account'
            # message = render_to_string('account_activation_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': account_activation_token.make_token(user),
            # })
            # user.email_user(subject, message)



@csrf_exempt
def loginView(request: HttpRequest):
    if request.method == 'POST':
        form = LoginForm(json.loads(request.body))
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponse(json.dumps({'message':'success'}))
        else:
            return HttpResponse(json.dumps(geterrorResponse(form)))



def logoutView(request: HttpRequest):
    if request.method == 'POST':
        logout(request)
        return HttpResponse(json.dumps({'message':'success'}))

@login_required
def HelloView(request: HttpRequest):
    return HttpResponse("hello world")