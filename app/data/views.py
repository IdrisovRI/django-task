import rest_framework.response as rest_response
from rest_framework import views, status
from rest_framework.permissions import AllowAny
from data.forms import DataForm
from django.db.models import Sum, Count
from data.models import Data


class AddDataView(views.APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def __validate_data(data_str: str):
        try:
            data_list = data_str.split(";")

            for data_element in data_list:
                a, b = tuple(map(int, data_element.split(",")))

                if type(a) != int or type(b) != int:
                    return False
        except TypeError:
            return False

        return True

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            request_data = request.data
            data_str = request_data['data']

            if not self.__validate_data(data_str):
                return rest_response.Response({"error": "Bad data format."}, status=status.HTTP_400_BAD_REQUEST)

            data_list = data_str.split(";")
            number_of_elements = 0
            for data_element in data_list:
                a, b = tuple(map(int, data_element.split(",")))

                form = DataForm({"a": a, "b": b})
                if form.is_valid():
                    form.save()
                    number_of_elements += 1

            return rest_response.Response(
                {"result": f"Added {number_of_elements} elements."},
                status=status.HTTP_200_OK
            )

        return rest_response.Response({"error": "Bad request or data format."}, status=status.HTTP_400_BAD_REQUEST)


class GetDataView(views.APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def __prepare_response(data):
        result_list = []

        for element in data:
            result_list.append(f"{element['a']},{element['sum_data']}")

        result = ""
        if result_list:
            result = ";".join(result_list)

        return result

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            a = request.GET.get('a', None)
            b = request.GET.get('b', None)

            if not a and not b:
                return rest_response.Response({"error": "Bad request or data format."},
                                              status=status.HTTP_400_BAD_REQUEST)

            data_objects = Data.objects.values("a")

            if a:
                data_objects = data_objects.filter(a__gte=a)

            data = data_objects.annotate(sum_data=Sum("b")).values("a", "sum_data")

            if b:
                data = data.filter(sum_data__gte=b)

            data = data.order_by("a")

            return rest_response.Response({"result": self.__prepare_response(data)}, status=status.HTTP_200_OK)

        return rest_response.Response({"error": "Bad request or data format."}, status=status.HTTP_400_BAD_REQUEST)
