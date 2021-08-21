from manim import *

class MainScene(Scene):
    def construct(self):
        l1 = Line([-3,0,0], [-1,0,0]).set_color(BLUE)
        l2 = Line([1,0,0], [3,0,0]).set_color(BLUE)

        a1_invisible = Arc(arc_center=[0,0,0], start_angle=PI, angle=-PI/2).set_color(BLUE)
        a2_invisible = Arc(arc_center=[0,0,0], start_angle=PI/2, angle=-PI/2).set_color(BLUE)
        a_visible = Arc(arc_center=[0,0,0], start_angle=PI, angle=-PI).set_color(BLUE)

        ball1 = Dot([-3,0,0])

        wire1 = VGroup(l1, a1_invisible, a2_invisible, a_visible, l2)

        brace = BraceBetweenPoints([-3,0,0], [3,0,0], direction=[0,-1,0])
        btext = brace.get_text("S")
        b1 = VGroup(brace, btext)

        #ball1 moves through wire1
        self.play(Write(wire1 - a1_invisible - a2_invisible), Write(ball1))
        self.play(MoveAlongPath(ball1, l1), run_time=1, rate_func=linear)
        self.play(MoveAlongPath(ball1, a1_invisible), run_time=0.5, rate_func=rate_functions.ease_out_sine)
        self.play(Write(brace), Write(btext))
        self.play(MoveAlongPath(ball1, a2_invisible), run_time=0.5, rate_func=rate_functions.ease_in_sine)
        self.play(MoveAlongPath(ball1, l2), run_time=1, rate_func=linear)
        #self.play(Unwrite(brace_label))

        #Works with a flip
        #l1_2 = l1.copy()
        #l2_2 = l2.copy()
        #a1_2_invisible = a1_invisible.copy()
        #a2_2_invisible = a2_invisible.copy()
        #a_2_visible = a_visible.copy()

        l2_2 = Line([-1,0,0], [-3,0,0])
        l1_2 = Line([3,0,0], [1,0,0])
        a2_2_invisible = Arc(arc_center=[0,0,0], start_angle=PI/2, angle=PI/2)
        a1_2_invisible = Arc(arc_center=[0,0,0], start_angle=0, angle=PI/2)
        a_2_visible = Arc(arc_center=[0,0,0], start_angle=0, angle=PI)


        wire2 = VGroup(l1_2, a1_2_invisible, a2_2_invisible, a_2_visible, l2_2).set_color(RED)
        ball2 = Dot([-3,0,0])

        wire1 += ball1; wire1

        self.play(ApplyMethod(wire1.shift, UP), ApplyMethod(b1.shift, DOWN), run_time=0.75)
        self.play(Write(wire2))
        self.play(ApplyMethod(wire2.shift, DOWN), run_time=0.75)


        #Here is the 8th second, so the question will need to appear if we want to sync video and audio
        question=Tex(r"Which ball will finish first?").scale(1.3)
        #self.play(Write(question.to_corner(UP)))


        self.play(Write(question.to_corner(UP)), wire2.animate.rotate(angle=PI, axis=[0,0,1]))

        #the flip with which it works
        #self.play(wire2.animate.rotate(angle=PI, axis=[0,1,0]))

        self.play(Write(ball2))
        wire2 += ball2; wire2

        #ball2 moves through wire2
        self.play(MoveAlongPath(ball2, l1_2), run_time=1, rate_func=linear)
        self.play(MoveAlongPath(ball2, a1_2_invisible), run_time=0.5, rate_func=rate_functions.ease_in_sine)
        self.play(MoveAlongPath(ball2, a2_2_invisible), run_time=0.5, rate_func=rate_functions.ease_out_sine)
        self.play(MoveAlongPath(ball2, l2_2), run_time=1, rate_func=linear)



        self.wait(0.5)

        self.play(Unwrite(question))

        #Make them small and move them to the top left corner
        self.play(ApplyMethod(wire1.scale, 0.25), ApplyMethod(wire2.scale, 0.25), Unwrite(b1), run_time=0.75)
        self.play(ApplyMethod(wire1.move_to, [-3.5, 3.5, 0]), wire2.animate.move_to([3.5, 3.5, 0]), run_time=0.75)

        '''
        question=Tex(r"Which ball will finish first?").scale(1.3)
        self.play(Write(question))

        self.wait(0.5)

        self.play(Unwrite(question))
        '''

        ax1 = Axes(
            x_range=[0, 7, 1],  # step size determines num_decimal_places.
            y_range=[0, 6, 1],
            x_length=6,
            y_length=5,
            tips=False,
        )

        ax2 = Axes(
            x_range=[0, 7, 1],  # step size determines num_decimal_places.
            y_range=[0, 6, 1],
            x_length=6,
            y_length=5,
            tips=False,
        )

        ax1.move_to([-3.5,0,0])
        ax2.move_to([3.5,0,0])

        g1 = ax1.get_graph(
                    lambda x: 3 if (x < 2 or x > 4) else (-np.sqrt(1-(x-3)**2) + 3),
                    x_range=[0,6],
                    use_smoothing=False,
                    color=BLUE,
                )

        g2 = ax2.get_graph(
                    lambda x: 3 if (x < 2 or x > 4) else (np.sqrt(1-(x-3)**2) + 3),
                    x_range=[0,6],
                    use_smoothing=False,
                    color=RED,
                )

        self.wait(8)

        y1_label = ax1.get_y_axis_label("v")
        x1_label = ax1.get_x_axis_label("t")
        y2_label = ax2.get_y_axis_label("v")
        x2_label = ax2.get_x_axis_label("t")
        ax_labels = VGroup(x1_label, y1_label, x2_label, y2_label)

        vi1 = MathTex(r'v_i').next_to(ax1.c2p(0,3), LEFT).scale(0.75)
        vi2 = MathTex(r'v_i').next_to(ax2.c2p(0,3), LEFT).scale(0.75)

        self.play(Write(ax1), Write(ax2), Write(ax_labels))
        self.play(Create(g1), Create(g2), Write(vi1), Write(vi2))

        self.wait(12)

        vtS = Tex(r'$v\cdot{t} = S$').to_corner(DOWN).scale(1.5)

        area1 = ax1.get_area(g1, color=['#58C4DD', '#5CD0B3'], dx_scaling=1)
        area2 = ax2.get_area(g2, color=['#FC6255', '#C55F73'], dx_scaling=1)

        s1 = Tex(r'$S$').move_to(ax1.c2p(5.5,4)).scale(1.5)
        s2 = Tex(r'$S$').move_to(ax2.c2p(5.5,4)).scale(1.5)

        self.play(Write(vtS))
        self.play(Write(area2), Write(area1))
        self.play(Write(s1), Write(s2))

        elipse = ax1.get_graph(
            lambda x: 3 if (x < 2 or x > 5) else (-np.sqrt(1-((x-3.5)/1.5)**2) + 3),
            use_smoothing=False,
            x_range=[0,7],
            color=BLUE

        )
        area_elipse = ax1.get_area(elipse, color=['#58C4DD', '#5CD0B3'], dx_scaling=1)

        self.play(Unwrite(vtS))
        self.wait(1)

        line_1 = ax1.get_vertical_line(ax1.input_to_graph_point(7, elipse), color=YELLOW)
        line_2 = ax2.get_vertical_line(ax2.input_to_graph_point(6, g2), color=YELLOW)

        t1 = Tex(r'$t_1$').next_to(ax1.c2p(7,0), DOWN, buff=0.5).scale(1.5)
        t2 = Tex(r'$t_2$').next_to(ax2.c2p(6,0), DOWN, buff=0.5).scale(1.5)
        greater_than = Tex(r'$>$').next_to(ax2.c2p(2.5,0), DOWN, buff=0.5).scale(1.5)


        self.play(FadeTransform(g1, elipse),FadeTransform(area1, area_elipse))

        self.wait(5)
        self.play(Write(line_1), Write(line_2), Write(t1), Write(t2), Write(greater_than))

        #Excuse my naming
        t1t1g = VGroup(t1, t2, greater_than)
        t_text = Tex(r'$t_1 > t_2$').scale(1.5).to_corner(DOWN)
        t1_grt_t2 = VGroup(t_text)

        #Making them into VGroups makes the texts into vectorized "objects" - vmobjects (technically groups),
        #which can be transformed with matching parts, so it doesn't look ugly
        self.play(TransformMatchingShapes(t1t1g, t1_grt_t2))
        self.wait(1)

        #Fade Out everything and put into focus wire2 - our winner
        self.play(FadeOut(ax1), FadeOut(ax2), FadeOut(elipse), FadeOut(g2), FadeOut(ax_labels), FadeOut(vi1), FadeOut(vi2), FadeOut(area_elipse), FadeOut(area2), FadeOut(s1), FadeOut(s2), FadeOut(line_1), FadeOut(line_2), FadeOut(t1_grt_t2))

        self.play(ApplyMethod(wire2.move_to, [0,1,0]), FadeOut(wire1), run_time=1)
        self.play(ApplyMethod(wire2.scale, 4, run_time=1), Write(Tex(r'The second ball finished first!').scale(1.5).next_to(wire2, DOWN, buff=1)))
        self.wait(0.2)


class Thumbnail(Scene):
    def construct(self):

        l1 = Line([-3,0,0], [-1,0,0]).set_color(BLUE)
        l2 = Line([1,0,0], [3,0,0]).set_color(BLUE)
        ball1 = Dot([-3,0,0])

        ball2 = Dot([-3,0,0])

        arc = Arc(arc_center=[0,0,0], start_angle=PI, angle=-PI).set_color(BLUE)
        wire1 = VGroup(l1, arc, l2)

        wire2 = wire1.copy().set_color(RED)
        wire1 += ball1; wire1

        wire1.shift(0.75 * UP)
        wire2.shift(DOWN)
        wire2.rotate(angle=PI, axis=[0,0,1])

        wire2 += ball2; wire2

        wire2.shift(1.5 * DOWN)

        question = Tex(r'Which ball will reach the end first?').scale(1.5).to_edge(UP)

        self.add(wire1.scale(1.5), wire2.scale(1.5), question)

class ProfilePic(Scene):
    def construct(self):
        huh = Tex(r'$Huh?$').scale(4).move_to([0,0,0])
        self.add(huh)
