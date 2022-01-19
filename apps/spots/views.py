from django.shortcuts import render
from .models import Organization, Parkingspot, Catparking, PublicUser, Getdata
from django.http import JsonResponse

# Create your views here.
def availableseats(request):
    #print("hi1")
    #print(Organization.objects.values_list(orgname))
    #print(*Organization._meta.get_fields(),)
    #print(Organization.orgname)
    if request.method == 'POST':
        parks =  Parkingspot.objects.all()
        for p in parks:
            p.spotlat = 43
            p.save()
            print(p.spotlat, p.spotlong)
    return render(request,'spots/hi.html')

def saveseat(request):
    if request.method == 'POST':
        spot_id = request.POST.get('spot_id')
        gps_long = request.POST.get('gps_long')
        gps_lat = request.POST.get('gps_lat')

        try:
            sp = Parkingspot.objects.get(spotlat=gps_lat, spotlong=gps_long)
            #print(sp.spotid)
            if(sp.status == 'free'):
                sp.status = 'occupied'
                sp.save()
                responseData = {
                    'id': spot_id,
                    'status': 'OK',
                }
            else:
                responseData = {
                    'id': spot_id,
                    'status': 'Taken',
                }

        except:
            responseData = {
                'id': spot_id,
                'status': 'Wrong Coordinates',
            }
        
        return JsonResponse(responseData)
    return render(request,'spots/hi.html')

def change(request):
    
    if request.method == 'POST':
        spot_id = request.POST.get('spot_id')

        try:
            sp = Parkingspot.objects.get(spotid=spot_id)

            if(sp.status == 'free'):
                sp.status = 'occupied'
                sp.save()
                responseData = {
                    'id': spot_id,
                    'status': 'Changed to occupied',
                }
            elif (sp.status == 'occupied'):
                sp.status = 'free'
                sp.save()                
                responseData = {
                    'id': spot_id,
                    'status': 'Changed to free',
                }
            else:
                responseData = {
                    'id': spot_id,
                    'status': 'Not available',     
                }

        except:
            responseData = {
                'id': spot_id,
                'status': 'Wrong ID',
            }
        
        return JsonResponse(responseData)
    return render(request,'spots/hi.html')

def savedata(request):
    if request.method == 'POST':
        st = ''
        for key, value in request.POST.items():
            st += ('Key: %s' % (key) ) 
            # print(f'Key: {key}') in Python >= 3.7
            st += ('Value %s' % (value) )
        sentData = Getdata.objects.create(datatext =st)
    return render(request,'spots/hi.html')