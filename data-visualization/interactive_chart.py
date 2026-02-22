import plotly.graph_objects as go

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue_2023 = [12000, 15000, 19000, 17000, 21000, 24000,
                20000, 23000, 18000, 25000, 28000, 32000]
revenue_2024 = [15000, 18200, 22000, 19500, 24000, 27500,
                23000, 25800, 21000, 28000, 31000, 35000]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=months, y=revenue_2023,
    mode="lines+markers",
    name="2023",
    line=dict(color="royalblue", width=2),
    marker=dict(size=7),
))

fig.add_trace(go.Scatter(
    x=months, y=revenue_2024,
    mode="lines+markers",
    name="2024",
    line=dict(color="tomato", width=2),
    marker=dict(size=7),
))

fig.update_layout(
    title="Monthly Revenue: 2023 vs 2024",
    xaxis_title="Month",
    yaxis_title="Revenue ($)",
    yaxis_tickformat="$,.0f",
    hovermode="x unified",
    template="plotly_white",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
)

fig.write_html("interactive_chart.html")
fig.show()
print("Interactive chart saved to interactive_chart.html")
