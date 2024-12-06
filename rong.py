# from manim import *

# class FourierImageProcessing(Scene):
#     def construct(self):
#         # Title Animation
#         title = Text("Image Processing using Fourier Transform", font_size=80, gradient=(BLUE, PURPLE)).scale(0.8)
#         self.play(Write(title))
#         self.wait(1)
#         self.play(title.animate.to_edge(UP))
#         self.wait(1)
        
#         # Displaying Image
#         image = ImageMobject("snake.jpg").scale(1.5)
#         self.play(FadeIn(image))
#         self.wait(1)
        
#         # Breaking Image into Grids (Pixel Representation)
#         self.play(image.animate.scale(0.8))
#         grid = VGroup(*[
#             VGroup(*[Square(side_length=0.2).set_stroke(GREY, 0.5) for _ in range(30)])
#             for _ in range(30)
#         ]).arrange_in_grid(buff=0).move_to(image)
        
#         self.play(Create(grid), run_time=3)
#         self.wait(1)

#         # Zoom into One Pixel
#         pixel = grid[15000][15000]
#         zoomed_pixel = pixel.copy().scale(3).move_to(ORIGIN)
#         intensity_text = Text("Intensity = f(x, y)", font_size=24).next_to(zoomed_pixel, DOWN)

#         self.play(FocusOn(pixel), ReplacementTransform(pixel, zoomed_pixel))
#         self.play(Write(intensity_text))
#         self.wait(2)

#         self.play(FadeOut(zoomed_pixel), FadeOut(intensity_text))
#         self.wait(1)

#         # Fourier Transform Application
#         transform_text = Text("Applying Fourier Transform", font_size=28)
#         self.play(Write(transform_text))
#         self.wait(1)
#         self.play(FadeOut(transform_text))

#         # Show Processed Image
#         processed_image = ImageMobject("processed_snake.jpg").scale(1.5)
#         self.play(FadeTransform(image, processed_image))
#         self.wait(2)

#         # Applications of Image Processing
#         applications = VGroup(
#             Text("Low-pass filter: Retain low frequencies (blur the image).", font_size=24),
#             Text("High-pass filter: Retain high frequencies (enhance edges).", font_size=24),
#             Text("Band-pass filter: Retain frequencies within a range.", font_size=24),
#             Text("Compression: Retain most significant frequencies.", font_size=24)
#         ).arrange(DOWN, aligned_edge=LEFT).scale(0.8).to_edge(DOWN)
        
#         self.play(Write(applications))
#         self.wait(3)
