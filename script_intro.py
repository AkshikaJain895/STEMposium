from manim import *

class SignalExplanation(Scene):
    def construct(self):
        title = Text("What is a Signal?",font_size = 40,gradient=(BLUE,PURPLE))
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Signal description text
        description = Text(
            "A signal is any quantity that varies with time.", 
            font_size=24
        ).next_to(title, DOWN, buff=0.5)
        self.play(Write(description))
        self.wait(2)

        # Display moving arrow along the x-axis (sine wave)
        # Create axes
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-1.5, 1.5, 0.5],
            axis_config={"include_numbers": True},
        ).to_edge(UP)


        # Add axis labels
        x_label = axes.get_x_axis_label("Time")
        y_label = axes.get_y_axis_label("Amplitude")
        self.play(Create(axes), Write(x_label), Write(y_label))

        # Plot sin(x) graph
        sine_wave = axes.plot(lambda x: np.sin(x), color=BLUE)
       
        self.play(Create(sine_wave))

        # Add an arrow that slides through the x-axis
        tracker = ValueTracker(0)  # Tracks the x-coordinate of the arrow
        arrow = always_redraw(
            lambda: Arrow(
                start=axes.c2p(tracker.get_value(), 0),  # Base of arrow at x-axis
                end=axes.c2p(tracker.get_value(), np.sin(tracker.get_value())),  # Tip touches the sine graph
                color=YELLOW,
                max_tip_length_to_length_ratio=0.2,
            )
        )

        # Add all elements to the scene
        # self.play(Create(axes), Write(labels))
        # self.play(Create(sine_wave), Write(sine_label))
        self.add(arrow)

        # Animate the arrow moving along the graph
        self.play(tracker.animate.set_value(2 * PI), run_time=10, rate_func=linear)

        # Wait for a moment at the end
        self.wait(2)
        self.play(FadeOut(*self.mobjects))
        # Display images for each signal type (Sound Wave, Stock Price, AQI)
        sound_wave_img = ImageMobject("sound_wave.png").scale(0.9).to_edge(ORIGIN)
        stock_price_img = ImageMobject("stock_price.png").scale(0.9).to_edge(ORIGIN)
        aqi_img = ImageMobject("aqi.png").scale(0.9).to_edge(ORIGIN)
        # Show text for examples of signals (sound wave, stock price, AQI)
        sound_wave_text = Text("Sound Wave").scale(0.7).next_to(sound_wave_img, LEFT, buff=0.5)
        stock_price_text = Text("Stock Price").scale(0.7).next_to(stock_price_img,LEFT, buff=0.5)
        aqi_text = Text("AQI Levels").scale(0.7).next_to(aqi_img, LEFT, buff=0.5)

    

        self.play(Write(sound_wave_text))
        self.play(FadeIn(sound_wave_img))
        self.play(FadeOut(sound_wave_img),FadeOut(sound_wave_text))
        self.play(Write(stock_price_text))
        self.play(FadeIn(stock_price_img))
        self.play(FadeOut(stock_price_img),FadeOut(stock_price_text))
        self.play(Write(aqi_text))
        self.play(FadeIn(aqi_img))
        self.play(FadeOut(aqi_img),FadeOut(aqi_text))

        # self.play( Write(stock_price_text))
        # self.play( FadeIn(stock_price_img))

        # Display clock animation with moving hands to represent time
        # clock = Clock(radius=1, time=0)
        # self.play(Create(clock))
        # self.wait(1)

        # self.play(clock.animate.shift(UP*2), run_time=3)
        # self.wait(1)

        # # Final summary text
        # final_text = Text(
        #     "All these are examples of a quantity varying with time.", 
        #     font_size=24
        # ).next_to(aqi_img, DOWN, buff=0.5)
        # self.play(Write(final_text))
        self.wait(2)


