
df = pd.read_csv("info_about_players.csv")
# st.dataframe(df)


st.sidebar.title("Chess")

name = st.sidebar.selectbox("Player Name",df["name"].unique())
country = df[df["name"] == name]["country"].values[0].upper()
rating = df[df["name"] == name]["fide"].values[0].astype(int)
followers = df[df["name"] == name]["followers"].values[0].astype(int)
league = df[df["name"] == name]["league"].values[0].upper()
joined = df[df["name"] == name]["joined"].values[0].astype(int)


current_rapid_rating = df[df["name"] == name]["current_rapid_rating"].values[0]
highest_rapid_rating = df[df["name"] == name]["highest_rapid_rating"].values[0]

rapid_win= df[df["name"] == name]["rapid_win"].values[0]
rapid_draw= df[df["name"] == name]["rapid_draw"].values[0]
rapid_loss= df[df["name"] == name]["rapid_loss"].values[0]

data = pd.DataFrame({
    "highest_rapid_rating": [highest_rapid_rating],
    "current_rapid_rating": [current_rapid_rating],
    "rapid_win": [rapid_win],
    "rapid_draw": [rapid_draw],
    "rapid_loss": [rapid_loss]
})

current_blitz_rating = df[df["name"] == name]["current_blitz_rating"].values[0]
highest_blitz_rating = (df[df["name"] == name]["highest_blitz_rating"].values[0])

blitz_win= df[df["name"] == name]["blitz_win"].values[0]
blitz_draw= df[df["name"] == name]["blitz_draw"].values[0]
blitz_loss= df[df["name"] == name]["blitz_loss"].values[0]


blitz = pd.DataFrame({
    "current_blitz_rating": [current_blitz_rating],
    "highest_blitz_rating": [highest_blitz_rating],
    "blitz_win": [blitz_win],
    "blitz_draw": [blitz_draw],
    "blitz_loss": [blitz_loss]
})





st.title("Grand Master" " " + name )
st.header(country)

col1 , col2 , col3 , col4 = st.columns(4)
with col2:
    st.header("Rating")
    st.subheader(rating)
with col3:
    st. header("Followers")
    st.subheader(followers)
with col1:
    st. header("League")
    st.subheader(league)
with col4:
    st.header("Joined")
    st.subheader(joined)



blitz_transposed = blitz.T

# Create the heatmap using Seaborn's heatmap with the 'viridis' color palette
fig1, ax = plt.subplots()

sns.heatmap(blitz_transposed, cmap='tab20b', annot=True, fmt='.1f',cbar=False)
plt.xticks([])

# Display the heatmap using st.pyplot
st.header("BLITZ RECORD")
st.pyplot(fig1,use_container_width=True)

data_transposed = data.T

# Create the heatmap using Seaborn's heatmap with the 'viridis' color palette
fig2, ax = plt.subplots()

sns.heatmap(data_transposed, cmap='seismic', annot=True, fmt='.1f',cbar=False)
plt.xticks([])

# Display the heatmap using st.pyplot
st.header("RAPID RECORD")
st.pyplot(fig2,use_container_width=True)