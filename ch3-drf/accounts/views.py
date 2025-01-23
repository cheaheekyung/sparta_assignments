from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerialize
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegisterSerialize(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입 완료"}, status=201)
        return Response(serializer.errors, status=400)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist()  # 토큰 블랙리스트에 추가 (무효화)

            return Response(
                {"message": "로그아웃!"}, status=status.HTTP_205_RESET_CONTENT
            )
        except Exception as e:
            return Response(
                {"error": "잘못된 토큰입니다."}, status=status.HTTP_400_BAD_REQUEST
            )


class UserDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = request.user
        user.delete()  # 계정 완전히 삭제
        return Response(
            {"message": "회원탈퇴가 완료되었습니다."},
            status=status.HTTP_204_NO_CONTENT,
        )
