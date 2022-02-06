<template>
	<div class="flex h-screen">
		<div 
			v-if="feed"
			class="m-auto"
		>
			<Feed 
				:feed="feed"
			/>
			<div class="m-auto">
				<div>
					<Button
						class="float-left" 
						icon="chevron-left" 
						@click="$resources.fetchFeed.submit({
							previous:true
						})"
					/>
					<Button
						class="float-right" 
						icon="chevron-right" 
						@click="$resources.fetchFeed.submit()"
					/>
				</div>
			</div>
		</div>
		<LoadingText v-else text="Fetching feeds..." class="p-5"/>
	</div>
</template>

<script>
import Feed from './Feed.vue'
import { LoadingText } from 'frappe-ui'

export default {
	name: 'Feeds',
	components: {
		Feed,
		LoadingText
	},
	resources: {
		fetchFeed() {
			return {
				method: 'zineify.api.feeds.get_user_feed',
				auto: true
			}
		}
	},
	computed: {
		feed() {
			return this.$resources.fetchFeed.data ? this.$resources.fetchFeed.data : null;
		}
	}
}
</script>

<style>

</style>