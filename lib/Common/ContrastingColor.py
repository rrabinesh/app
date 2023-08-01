# <?php

# class ContrastingColor
# {
#     /**
#      * @var string|null
#      */
#     private $sourceColor;

#     public function __construct($sourceColor)
#     {
#         $this->sourceColor = str_replace('#', '', $sourceColor);
#     }

#     public function GetHex()
#     {
#         // http://24ways.org/2010/calculating-color-contrast/
#         $r = hexdec(substr($this->sourceColor, 0, 2));
#         $g = hexdec(substr($this->sourceColor, 2, 2));
#         $b = hexdec(substr($this->sourceColor, 4, 2));
#         $yiq = (($r*299)+($g*587)+($b*114))/1000;
#         return ($yiq >= 128) ? '#000000' : '#FFFFFF';
#     }

#     public function __toString()
#     {
#         return $this->GetHex();
#     }
# }

# class AdjustedColor
# {
#     /**
#      * @var string|null
#      */
#     private $sourceColor;

#     /**
#      * @var string|null
#      */
#     private $steps;

#     public function __construct($sourceColor, $steps = 50)
#     {
#         $this->sourceColor = str_replace('#', '', $sourceColor);
#         $this->steps = $steps;
#     }

#     public function GetHex()
#     {
#         if (!preg_match('/^#?([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i', $this->sourceColor, $parts)) {
#             return '';
#         }
#         $out = "";
#         for ($i = 1; $i <= 3; $i++) {
#             $parts[$i] = hexdec($parts[$i]);
#             $parts[$i] = round($parts[$i] * $this->steps/100);
#             $out .= str_pad(dechex($parts[$i]), 2, '0', STR_PAD_LEFT);
#         }
#         return '#' . $out;
#     }

#     public function __toString()
#     {
#         return $this->GetHex();
#     }
# }

from fastapi import FastAPI

app = FastAPI()

class ContrastingColor:
    def __init__(self, source_color: str):
        self.source_color = source_color.lstrip('#')

    def get_hex(self):
        # http://24ways.org/2010/calculating-color-contrast/
        r = int(self.source_color[0:2], 16)
        g = int(self.source_color[2:4], 16)
        b = int(self.source_color[4:6], 16)
        yiq = ((r * 299) + (g * 587) + (b * 114)) / 1000
        return '#000000' if yiq >= 128 else '#FFFFFF'

    def __str__(self):
        return self.get_hex()

class AdjustedColor:
    def __init__(self, source_color: str, steps=50):
        self.source_color = source_color.lstrip('#')
        self.steps = steps

    def get_hex(self):
        try:
            r = int(self.source_color[0:2], 16)
            g = int(self.source_color[2:4], 16)
            b = int(self.source_color[4:6], 16)
        except ValueError:
            return ''

        out = ""
        for color in [r, g, b]:
            color = round(color * self.steps / 100)
            out += f"{color:02X}"
        return '#' + out

    def __str__(self):
        return self.get_hex()

# Create instances of ContrastingColor and AdjustedColor
contrasting_color = ContrastingColor("#FF0000")
adjusted_color = AdjustedColor("#00FF00")

@app.get("/contrasting_color")
def get_contrasting_color():
    return {"contrasting_color": str(contrasting_color)}

@app.get("/adjusted_color")
def get_adjusted_color():
    return {"adjusted_color": str(adjusted_color)}

