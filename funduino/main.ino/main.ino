#include <Colorduino.h>

/* Gamma correction */
const uint8_t PROGMEM gamma8[] = {
  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  1,
  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2,  2,
  2,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  5,  5,  5,
  5,  6,  6,  6,  6,  7,  7,  7,  7,  8,  8,  8,  9,  9,  9, 10,
  10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16,
  17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 24, 24, 25,
  25, 26, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33, 34, 35, 35, 36,
  37, 38, 39, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50,
  51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68,
  69, 70, 72, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89,
  90, 92, 93, 95, 96, 98, 99, 101, 102, 104, 105, 107, 109, 110, 112, 114,
  115, 117, 119, 120, 122, 124, 126, 127, 129, 131, 133, 135, 137, 138, 140, 142,
  144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 167, 169, 171, 173, 175,
  177, 180, 182, 184, 186, 189, 191, 193, 196, 198, 200, 203, 205, 208, 210, 213,
  215, 218, 220, 223, 225, 228, 231, 233, 236, 239, 241, 244, 247, 249, 252, 255
};

/*
   0 - empty
   1 - 2^1 = 2
   2 - 2^2 = 4
   ...
   9 - 2^9 = 512
   A - 2^10 = 1024
   B - 2^11 = 2048
*/

void setup() {
  while (!Serial);
  Serial.begin(9600);


  Colorduino.Init();
}

void setColor(unsigned char x, unsigned char y, unsigned char r, unsigned char g, unsigned char b) {
  Colorduino.SetPixel(x, y, pgm_read_byte(&gamma8[r]), pgm_read_byte(&gamma8[g]), pgm_read_byte(&gamma8[b]));
  Colorduino.SetPixel(x + 1, y, pgm_read_byte(&gamma8[r]), pgm_read_byte(&gamma8[g]), pgm_read_byte(&gamma8[b]));
  Colorduino.SetPixel(x, y + 1, pgm_read_byte(&gamma8[r]), pgm_read_byte(&gamma8[g]), pgm_read_byte(&gamma8[b]));
  Colorduino.SetPixel(x + 1, y + 1, pgm_read_byte(&gamma8[r]), pgm_read_byte(&gamma8[g]), pgm_read_byte(&gamma8[b]));
}

void loop() {
  unsigned char fields[16];
  unsigned char i = 0;
  while (Serial.available()) {
    delay(3);  //delay to allow buffer to fill
    if (Serial.available() > 0) {
      fields[i++] = Serial.read();  //gets one byte from serial buffer
    }
  }
  if (i == 16) {
    for (i = 0; i < 16; i++) {
      unsigned char x = 2 * (i % 4);
      unsigned char y = 2 * (i / 4);

      switch (fields[i]) {  // not sure that colors are described correctly
        case '0':
          setColor(x, y, 0, 0, 0); // nothing
          break;
        case '1':
          setColor(x, y, 255, 255, 0); // yellow
          break;
        case '2':
          setColor(x, y, 128, 0, 0); // maroon
          break;
        case '3':
          setColor(x, y, 128, 128, 0); // olive
          break;
        case '4':
          setColor(x, y, 0, 255, 0); // lime
          break;
        case '5':
          setColor(x, y, 0, 255, 255); // aqua
          break;
        case '6':
          setColor(x, y, 0, 0, 255); // blue
          break;
        case '7':
          setColor(x, y, 96, 0, 96); // navy
          break;
        case '8':
          setColor(x, y, 192, 0, 192); // purple
          break;
        case '9':
          setColor(x, y, 255, 152, 0); // orange
          break;
        case 'A':
          setColor(x, y, 255, 0, 0); // red
          break;
        case 'B':
          setColor(x, y, 255, 255, 255); // white
          break;
      }
    }
    Colorduino.FlipPage();
  }
}
