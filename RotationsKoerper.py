from manim import *

class RotationsKoerper(ThreeDScene):
    def construct(self):
        # Title
        title = Text("x-Achsen Rotationskörper")
        self.play(Write(title))
        self.wait(3)
        self.play(FadeOut(title))

        # Gliederung
        items = BulletedList(
            "1. Definition Rotationskörper",
            "2. Visuelle Darstellung",
            "3. Volumen Formel",
            font_size=36
        )
        self.play(FadeIn(items, shift=DOWN))
        self.wait(3)

        # Definition des ersten Punktes
        p1 = Text("Definition Rotationskörper", font_size=36)
        definition_text = """Ein Rotationskörper ist ein geometrischer Körper,
der entsteht, wenn eine zweidimensionale Fläche um eine Achse rotiert
(in dem Video explizit die x-Achse). Diese Rotation führt dazu, dass sich
die Punkte der Fläche in einem dreidimensionalen Raum bewegen und eine
geschlossene Oberfläche bilden."""
        definition = Text(definition_text, font_size=36)
        p1.to_edge(UL)
        definition.move_to(ORIGIN)
        definition.scale(0.8)

        self.play(FadeOut(items, shift=UP))
        self.play(Write(p1))
        self.play(Write(definition))
        self.wait(4)
        self.play(FadeOut(definition))

        # Wechsel zum nächsten Punkt "Visuelle Darstellung"
        p2 = Text("Visuelle Darstellung")
        p2.to_edge(UL)
        self.play(FadeOut(p1), FadeIn(p2))
        self.wait(2)

        # Visualisierung der Funktion
        axes = ThreeDAxes(
            x_range=[0, 4, 4],
            y_range=[0, 4, 4],
            z_range=[0, 8, 2],
        )
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)", z_label="")
        self.play(Create(axes), Write(labels))
        self.wait(1)

        def func(x):
            return 0.5 * x**2

        graph = axes.plot(func, color=YELLOW, x_range=[0, 3])
        graph_label = axes.get_graph_label(graph, label="f(x)=\\frac{1}{2}x^2", x_val=2)
        self.play(Create(graph), Write(graph_label))
        self.wait(2)

        area = axes.get_area(graph, x_range=[0, 3], color=GREEN, opacity=0.5)
        self.play(FadeIn(area))
        self.wait(2)

        self.move_camera(phi=75 * DEGREES, theta=-45 * DEGREES, distance=10, run_time=3)
        self.begin_ambient_camera_rotation(rate=0.2)

        surface = Surface(
            lambda u, v: axes.c2p(u, func(u) * np.cos(v), func(u) * np.sin(v)),
            u_range=[0, 3],
            v_range=[0, TAU],
            resolution=(32, 64),
            color=ORANGE,
        )
        surface.set_opacity(0.8)
        self.play(FadeIn(surface))
        self.wait(5)

        # Kamera vollständig zurücksetzen und Szene löschen
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=0, theta=-90 * DEGREES, distance=10, run_time=3)

        # Kamera manuell auf Standardwerte setzen
        self.renderer.camera.phi = 0
        self.renderer.camera.theta = -90 * DEGREES
        self.renderer.camera.gamma = 0  # Optional: Standardwert für Drehung um die Z-Achse
        self.renderer.camera.zoom = 1  # Standardzoom setzen
        self.wait(1)

        self.play(FadeOut(axes), FadeOut(graph), FadeOut(graph_label), FadeOut(area), FadeOut(surface), FadeOut(p2), FadeOut(labels))

        # Nächster Punkt: Volumenformel
        p3 = Text("Volumenformel", font_size=36)
        formula = MathTex(
            "V = \\pi \\int_a^b [f(x)]^2 \\, dx",
            font_size=48
        )
        explanation = Text(
            """Diese Formel berechnet das Volumen eines Rotationskörpers,
indem sie die Fläche unter der Funktion quadriert, summiert und 
mit π multipliziert.""",
            font_size=36
        )
        explanation.next_to(formula, DOWN, buff=0.5)

        self.play(Write(p3))
        p3.to_edge(UL)
        self.play(Write(formula))
        self.play(FadeIn(explanation))
        self.wait(5)

        # Alles löschen für den nächsten Punkt
        self.play(FadeOut(p3), FadeOut(formula), FadeOut(explanation))
