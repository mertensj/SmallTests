#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// If using software SPI (the default case):
#define OLED_MOSI   9
#define OLED_CLK   10
#define OLED_DC    11
#define OLED_CS    12
#define OLED_RESET 13
Adafruit_SSD1306 display(OLED_MOSI, OLED_CLK, OLED_DC, OLED_RESET, OLED_CS);

static const unsigned char PROGMEM logo64_bmp[] =
{ 
B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, 
B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, 
B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, 
B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, B00000000, 
B00000000, B00000000, B00000000, B00001100, B00000000, B00000000, B00000000, B00000000, 
B00000000, B00000000, B00000000, B01111011, B11101100, B00000000, B00000000, B00000000, 
B00000000, B00000000, B00000111, B00011111, B01111110, B00000000, B00000000, B00000000, 
B00000000, B00000000, B00011111, B11110111, B11111011, B11100000, B00000000, B00000000, 
B00000000, B00000000, B01111101, B11111101, B10111111, B11111100, B00000000, B00000000, 
B00000000, B00000011, B11110111, B11011111, B11101110, B11011010, B00000000, B00000000, 
B00000000, B00001111, B11111111, B11110110, B11111111, B11111111, B00000000, B00000000, 
B00000000, B00001111, B01101110, B11111111, B11111110, B11101111, B10000000, B00000000, 
B00000000, B00011111, B11111111, B11111111, B11011111, B11111110, B10000000, B00000000, 
B00000000, B00111101, B11111011, B10101101, B01110111, B11111011, B11000000, B00000000, 
B00000000, B00011111, B11101110, B11010111, B01001010, B10111111, B11000000, B00000000, 
B00000000, B00111111, B10110101, B00000000, B00000001, B01011111, B11100000, B00000000, 
B00000000, B00110111, B01010000, B01010000, B00010010, B01010110, B11100000, B00000000, 
B00000000, B00111111, B01010101, B00000100, B10000000, B00101111, B11100000, B00000000, 
B00000000, B00111101, B10100000, B01000000, B00100101, B01001011, B10110000, B00000000, 
B00000000, B00111110, B10010101, B00010010, B00001000, B00100111, B11100000, B00000000, 
B00000000, B00110111, B01010010, B01001000, B10100010, B10010110, B11100000, B00000000, 
B00000000, B00011111, B01001001, B00100010, B00001000, B01010111, B11100000, B00000000, 
B00000000, B00011111, B01010100, B01000000, B01000010, B00101011, B01100000, B00000000, 
B00000000, B00011101, B10100010, B00010100, B10001001, B01001011, B11100000, B00000000, 
B00000000, B00001111, B01011111, B11000010, B00110111, B10101011, B10100000, B00000000, 
B00000000, B00001110, B11110101, B01110100, B11011000, B01101001, B11000000, B00000000, 
B00000000, B00001111, B01010101, B10111010, B10111111, B10101101, B11000000, B00000000, 
B00000000, B00000110, B11011110, B11010100, B10100111, B11010101, B10011000, B00000000, 
B00000000, B00101111, B01110110, B01011010, B11010000, B01010101, B10100100, B00000000, 
B00000000, B00110110, B10101001, B00110100, B01010110, B10010011, B01001000, B00000000, 
B00000000, B01011011, B01010101, B01010101, B00100001, B00100101, B00000100, B00000000, 
B00000000, B00110110, B10100010, B01010000, B10101010, B01001010, B11010010, B00000000, 
B00000000, B00101110, B11010100, B10011101, B01000100, B00010010, B10001000, B00000000, 
B00000000, B00010101, B01010010, B01010101, B11010001, B01001010, B01000100, B00000000, 
B00000000, B00101011, B10101001, B01011110, B10101000, B00100101, B00101000, B00000000, 
B00000000, B00010101, B01010100, B10101010, B10100101, B00010101, B00010000, B00000000, 
B00000000, B00001011, B10101010, B01010101, B00100000, B10101010, B10100000, B00000000, 
B00000000, B00000101, B01101001, B01010100, B10011010, B01001000, B00000000, B00000000, 
B00000000, B00000000, B10110110, B10101001, B01000101, B01010110, B00000000, B00000000, 
B00000000, B00000000, B01011010, B10101111, B01111101, B01010010, B00000000, B00000000, 
B00000000, B00000000, B01101011, B01010000, B10000010, B10101010, B00000000, B00000000, 
B00000000, B10010010, B01010101, B01010111, B01101010, B01010100, B00000000, B00000000, 
B00000010, B00000000, B01101101, B01011001, B00101010, B10010100, B00000000, B00000000, 
B00000000, B00000000, B01010110, B10101010, B10010010, B01010100, B00000000, B00000000, 
B00001000, B00001000, B01110101, B01010101, B01001001, B01010100, B00000000, B00000000, 
B00000000, B01000001, B00101101, B10101010, B00101010, B10101000, B00000000, B00000000, 
B00000001, B00000000, B01110110, B10101010, B10101010, B10110100, B00000000, B00000000, 
B00010000, B00001000, B01011011, B01101010, B10101011, B01101010, B00000000, B00000000, 
B00000000, B00100001, B01010110, B11011101, B11110110, B10101010, B00000000, B00000000, 
B00000100, B10000000, B01101101, B10110111, B01011011, B10101100, B00000000, B00000000, 
B00100000, B00000010, B00110111, B01111010, B11101101, B01010110, B00000000, B00000000, 
B00000010, B00000000, B00101011, B11011111, B10110110, B10101010, B00000000, B00000000, 
B00000000, B00000001, B00101101, B01101010, B11011010, B10101100, B00000000, B00000000, 
B00000000, B00000000, B00101010, B10110101, B01010101, B01010100, B00000000, B00000000, 
B00000000, B00000010, B00010101, B11011010, B10101010, B10011000, B00000000, B00000000, 
B00000000, B00000000, B10000101, B01101010, B10101010, B01000000, B00000000, B00000000, 
B00000000, B00000000, B00001010, B10101101, B01010100, B10110000, B00000000, B00000000, 
B00000000, B00000010, B10010000, B01010010, B10101001, B01000000, B00000000, B00000000, 
B00000000, B00000000, B01000000, B00101010, B10010010, B10010000, B00000000, B00000000, 
B00000000, B00000000, B00001000, B00001010, B01001001, B00000000, B00000000, B00000000, 
B00000000, B00000000, B10100010, B10010101, B01010100, B00100000, B00000000, B00000000, 
B00000000, B00000000, B00000000, B00001010, B10000010, B01000000, B00000000, B00000000, 
B00000000, B00001000, B00101000, B00010001, B00101000, B00000000, B00000000, B00000000, 
B00000000, B00000000, B00000001, B00001010, B01001000, B01000000, B00000000, B00000000
};

void setup()   {                
  Serial.begin(9600);
  
  // by default, we'll generate the high voltage from the 3.3v line internally! (neat!)
  display.begin(SSD1306_SWITCHCAPVCC);
  // init done

  // miniature bitmap display
  display.clearDisplay();
  display.drawBitmap(32, 0,  logo64_bmp, 64, 64, 1);
  display.display();
}


void loop() {
  //display.startscrollright(0x00, 0x0F);
  //delay(4000);
  //display.stopscroll();

  //display.startscrollleft(0x00, 0x0F);
  //delay(4000);
  //display.stopscroll();
}





