# Dockerfile
FROM python:3.9

# 환경 변수 설정
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY auth/requirements.txt /app/
RUN pip install --upgrade pip \ 
    pip install -r requirements.txt

# 프로젝트 파일 복사
COPY auth /app/

# 애플리케이션 실행
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
