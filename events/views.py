from django.shortcuts import render
# from django.http import JsonResponse
# from .models import load_model
# # from .forms import ImageUploadForm
# import torch

# def predict(request):
#     if request.method == 'POST':
#         data = request.POST.get('input_data')
#         # 데이터 전처리 로직 수행
#         # ...

#         # PyTorch 모델 로드
#         model = load_model()

#         # 예측 수행
#         with torch.no_grad():
#             output = model(data)  # 모델에 데이터 전달 및 예측 수행

#         # 결과 반환
#         response_data = {'prediction': output.item()}  # 예측 결과를 JSON 형태로 반환
#         return JsonResponse(response_data)
#     else:
#         return JsonResponse({'error': 'Invalid request method'})

# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             uploaded_image = form.cleaned_data['image']
#             # 여기서 이미지를 저장하거나 모델에 전달할 수 있습니다.
#             # ...
#     else:
#         form = ImageUploadForm()
#     return render(request, 'upload.html', {'form': form})