# 2.9inch e-paper display (C) Demo.

import epd2in9b
from PIL import Image, ImageFont, ImageDraw

COLORED = 1
UNCOLORED = 0

def main():
    epd = epd2in9b.EPD()
    epd.init()

    # clear the frame buffer
    frame_black = [0xFF] * int(epd.width * epd.height / 8)
    frame_highlight = [0xFF] * int(epd.width * epd.height / 8)

    # For simplicity, the arguments are explicit numerical coordinates
    epd.draw_rectangle(frame_black, 10, 80, 50, 140, COLORED);
    epd.draw_line(frame_black, 10, 80, 50, 140, COLORED);
    epd.draw_line(frame_black, 50, 80, 10, 140, COLORED);
    epd.draw_circle(frame_black, 90, 110, 30, COLORED);
    epd.draw_filled_rectangle(frame_highlight, 10, 180, 50, 240, COLORED);
    epd.draw_filled_rectangle(frame_highlight, 0, 6, 128, 26, COLORED);
    epd.draw_filled_circle(frame_highlight, 90, 210, 30, COLORED);

    # write strings to the buffer
    font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 16)
    epd.draw_string_at(frame_black, 4, 30, "e-Paper Demo", font, COLORED)
    epd.draw_string_at(frame_highlight, 6, 10, "Hello world!", font, UNCOLORED)
    # display the frames
    epd.display_frame(frame_black, frame_highlight)

    # display images
    frame_black = epd.get_frame_buffer(Image.open('demo/black.bmp'))
    frame_highlight = epd.get_frame_buffer(Image.open('demo/highlight.bmp'))
    epd.display_frame(frame_black, frame_highlight)

    # You can get frame buffer from an image or import the buffer directly:
    #epd.display_frame(imagedata.IMAGE_BLACK, imagedata.IMAGE_HIGHLIGHT)

if __name__ == '__main__':
    main()
