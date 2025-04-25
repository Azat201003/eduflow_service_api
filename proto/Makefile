# Автоматическая генерация
all: 
	protoc --proto_path=./ --go_out=./../ --go-grpc_out=./../ ./*/*.proto
	python -m grpc_tools.protoc --proto_path=./ \
  --python_out=./../gen --grpc_python_out=./../gen \
  ./*/*.proto
