# <?php

# class ReservationRetryParameter
# {
#     public static $SKIP_CONFLICTS = "skipconflicts";
#     private $name;
#     private $value;

#     /**
#      * @param string $name
#      * @param string $value
#      */
#     public function __construct($name, $value)
#     {
#         $this->name = $name;
#         $this->value = $value;
#     }

#     /**
#      * @static
#      * @param $params string|string[]|null The result of $this->GetForm(FormKeys::RESERVATION_RETRY_PREFIX)
#      * @return array|AttributeFormElement[]
#      */
#     public static function GetParamsFromForm($params)
#     {
#         if (is_array($params)) {
#             $af = [];

#             foreach ($params as $name => $value) {
#                 $af[] = new ReservationRetryParameter($name, $value);
#             }

#             return $af;
#         }

#         return [];
#     }

#     /**
#      * @param string $parameterName
#      * @param ReservationRetryParameter[] $retryParameters
#      * @param null|IConvert $converter
#      * @return null|string
#      */
#     public static function GetValue($parameterName, $retryParameters, $converter = null)
#     {
#         if (!is_array($retryParameters)) {
#             return null;
#         }

#         if ($converter == null) {
#             $converter = new LowerCaseConverter();
#         }

#         /** @var ReservationRetryParameter $retryParameter */
#         foreach ($retryParameters as $retryParameter) {
#             if ($retryParameter->Name() == $parameterName) {
#                 return $converter->Convert($retryParameter->Value());
#             }
#         }

#         return null;
#     }

#     /**
#      * @return string
#      */
#     public function Name()
#     {
#         return $this->name;
#     }

#     /**
#      * @return string
#      */
#     public function Value()
#     {
#         return $this->value;
#     }
# }




class ReservationRetryParameter:
    SKIP_CONFLICTS = "skipconflicts"

    def __init__(self, name, value):
        self.name = name
        self.value = value

    @staticmethod
    def get_params_from_form(params):
        if isinstance(params, dict):
            return [ReservationRetryParameter(name, value) for name, value in params.items()]
        return []

    @staticmethod
    def get_value(parameter_name, retry_parameters, converter=None):
        if not isinstance(retry_parameters, list):
            return None

        if converter is None:
            converter = lambda x: x.lower()

        for retry_parameter in retry_parameters:
            if retry_parameter.name == parameter_name:
                return converter(retry_parameter.value)

        return None

    def name(self):
        return self.name

    def value(self):
        return self.value


