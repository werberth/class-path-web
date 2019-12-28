from django.urls import reverse_lazy as r
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views import generic

from . import base_views, forms, models

# FBVs

def signup(request):
    success_url = r('core:login')
    template_name = 'accounts/signup.html'
    user_form = forms.CustomUserCreationForm(initial={'is_admin': True})
    institution_form = forms.InstitutionForm()

    if request.method == "POST":
        user_form = forms.CustomUserCreationForm(request.POST)
        institution_form = forms.InstitutionForm(request.POST)

        if institution_form.is_valid() and user_form.is_valid():
            # create institution
            institution = institution_form.save()
            # create admin user
            user_form.cleaned_data['is_admin'] = True
            user = user_form.save()
            # define this user as admin of this that institution
            models.Admin.objects.create(user=user, institution=institution)
            return redirect(success_url)

    context = {
        'institution_form': institution_form,
        'user_form': user_form
    }
    return render(request, template_name, context)

# CBVs

@method_decorator(login_required, name='dispatch')
class CreateProgram(generic.CreateView):
    form_class = forms.ProgramForm
    success_url = r('core:dashboard')
    template_name = 'accounts/create_program.html'

    def form_valid(self, form):
        program = form.save(commit=False)
        program.institution = self.request.user.admin.institution
        self.object = program.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ListProgram(base_views.BaseProgramView, generic.ListView):
    template_name = 'accounts/program_list.html'
    context_object_name = 'programs'


@method_decorator(login_required, name='dispatch')
class UpdateProgram(base_views.BaseProgramView, generic.UpdateView):
    form_class = forms.ProgramForm
    success_url = r('accounts:list-program')
    template_name = 'accounts/update_program.html'
    context_object_name = 'program'


# define CBVs as FBVs
create_program = CreateProgram.as_view()
update_program = UpdateProgram.as_view()
list_program = ListProgram.as_view()
