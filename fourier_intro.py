from manim import *

class FourierIntro(Scene):
    def construct(self):
        # Title Text
        title = Text("Fourier Transform", font_size=80, gradient=(BLUE, PURPLE))
        title.to_edge(UP)

        # Subtitle Text
        subtitle = Text("STEMposium team: EverImagined?", font_size=40, color=WHITE)
        subtitle.next_to(title, DOWN)

        # Background Waves (Stylized Sine Waves)
        wave1 = FunctionGraph(lambda x: np.sin(2 * np.pi * x), x_range=[-7, 7], color=BLUE).scale(0.5)
        wave2 = FunctionGraph(lambda x: np.sin(4 * np.pi * x), x_range=[-7, 7], color=PURPLE).scale(0.5)
        waves = VGroup(wave1, wave2).arrange(DOWN, buff=0.5)

        # Animate Waves
        self.play(Create(wave1), run_time=2)
        self.play(Transform(wave1, wave2), run_time=2)
        self.play(FadeOut(wave1))

        # Animate Title and Subtitle
        self.play(Write(title), run_time=2)
        self.play(Write(subtitle), run_time=1.5)
        self.play(FadeOut(subtitle))

        # Add Dynamic Fourier Representation
        axes = Axes(
            x_range=[0, 6],
            y_range=[-1.5, 1.5],
            axis_config={"color": GREY},
        ).to_edge(DOWN)

        # Sine and Cosine Waves for Fourier Visualization
        sine_wave = axes.plot(lambda x: np.sin(2 * np.pi * x), color=BLUE, x_range=[0, 6])
        cosine_wave = axes.plot(lambda x: np.cos(2 * np.pi * x), color=PURPLE, x_range=[0, 6])
        combined_wave = axes.plot(lambda x: np.sin(2 * np.pi * x) + 0.5 * np.cos(4 * np.pi * x), color=GREEN, x_range=[0, 6])

        # Labels for the Waves
        sine_label = Text(r"sin(2πx)", color=BLUE).next_to(sine_wave, UP)
        cosine_label = Text(r"cos(2πx)", color=PURPLE).next_to(cosine_wave, DOWN)
        combined_label = Text("Superposition", font_size=30, color=GREEN).next_to(combined_wave, UP)

        # Animate Fourier Waves
        self.play(Create(axes), run_time=1.5)
        self.play(Create(sine_wave), Write(sine_label), run_time=2)
        self.play(Create(cosine_wave), Write(cosine_label), run_time=2)
        self.play(Transform(sine_wave, combined_wave), Transform(sine_label, combined_label), run_time=3)

        # Fade Out
        self.play(FadeOut(VGroup(axes, sine_wave, cosine_wave, sine_label, cosine_label, combined_label)))
        self.wait(1)

        # Closing Scene
        closing_text = Text("Let's Dive Into Fourier Transform!", font_size=50, gradient=(BLUE, PURPLE))
        self.play(Write(closing_text), run_time=2)
        self.play(FadeOut(closing_text), run_time=2)

